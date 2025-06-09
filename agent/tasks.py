import requests
import json
from celery import shared_task
from .models import WebsiteURL
from django.conf import settings

@shared_task
def process_website_url(url_id):
    """Background task to process website URL using Firecrawl API"""
    try:
        website_url = WebsiteURL.objects.get(url_id=url_id)
        website_url.status = 'processing'
        website_url.save()
        
        # Send initial webhook notification
        website_url.send_webhook_update('processing', 'Started processing website')
        
        # Firecrawl API configuration
        api_key = settings.FIRECRAWL_API_KEY
        api_url = "https://api.firecrawl.dev/v1/crawl"
        
        # Headers
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        
        # Request payload
        payload = {
            "url": website_url.url,
            "limit": 100,
            "webhook": {
                "url": settings.WEBHOOK_URL,
                "metadata": {
                    "url_id": website_url.url_id,
                    "user_id": website_url.uploaded_by.id
                },
                "events": ["started", "in_progress", "completed"],
                "metadata": {
                    "url_id": website_url.url_id,
                    "user_id": website_url.uploaded_by.id
                }
            }
        }
        
        try:
            # Make the POST request to Firecrawl API
            response = requests.post(api_url, headers=headers, json=payload)
            response.raise_for_status()
            
            # Parse the response
            result = response.json()
            
            # Update the model with initial results
            website_url.metadata = {
                'crawl_id': result.get('id'),
                'status': result.get('status'),
                'initial_response': result
            }
            website_url.save()
            
            # Send success webhook notification
            website_url.send_webhook_update(
                'processing',
                'Crawl initiated successfully',
                {
                    'crawl_id': result.get('id'),
                    'status': result.get('status')
                }
            )
            
        except requests.exceptions.RequestException as e:
            error_message = str(e)
            if hasattr(e, 'response') and e.response is not None:
                error_message = f"Status code: {e.response.status_code}, Response: {e.response.text}"
            
            website_url.status = 'failed'
            website_url.error_message = error_message
            website_url.save()
            
            # Send failure webhook notification
            website_url.send_webhook_update(
                'failed',
                f'Failed to initiate crawl: {error_message}'
            )
            raise
            
    except WebsiteURL.DoesNotExist:
        return f"Website URL with id {url_id} not found"
    except Exception as e:
        if website_url:
            website_url.status = 'failed'
            website_url.error_message = str(e)
            website_url.save()
            
            # Send failure webhook notification
            website_url.send_webhook_update(
                'failed',
                f'Failed to process website: {str(e)}'
            )
        return str(e)

@shared_task
def send_webhook_notification(webhook_url, data):
    """Send webhook notification to the specified URL"""
    try:
        response = requests.post(
            webhook_url,
            json=data,
            headers={'Content-Type': 'application/json'},
            timeout=5
        )
        response.raise_for_status()
        return True
    except Exception as e:
        # Log the webhook failure but don't raise the exception
        print(f"Failed to send webhook notification: {str(e)}")
        return False 