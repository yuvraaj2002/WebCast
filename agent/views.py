from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import WebsiteURL
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .tasks import process_website_url
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny

class URLProcessView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        try:
            # Get URL from request data
            url = request.data.get('url')
            
            if not url:
                return Response(
                    {'error': 'No URL provided'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Validate URL format
            validator = URLValidator()
            try:
                validator(url)
            except ValidationError:
                return Response(
                    {'error': 'Invalid URL format'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Create and save website URL
            website_url = WebsiteURL(
                url=url,
                uploaded_by=request.user
            )
            website_url.save()
            
            # Start background processing
            process_website_url.delay(website_url.url_id)
            
            return Response({
                'message': 'URL processing started',
                'url_id': website_url.url_id,
                'url': website_url.url,
                'title': website_url.title,
                'status': website_url.status,
                'added_by': request.user.id
            }, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class FirecrawlWebhookView(APIView):
    permission_classes = [AllowAny]  # Allow unauthenticated access for webhooks
    parser_classes = [JSONParser]
    
    def post(self, request, *args, **kwargs):
        try:
            # Extract metadata from the webhook payload
            metadata = request.data.get('metadata', {})
            url_id = metadata.get('url_id')
            
            if not url_id:
                return Response(
                    {'error': 'No URL ID in metadata'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Get the website URL instance
            website_url = WebsiteURL.objects.get(url_id=url_id)
            
            # Handle different event types
            event_type = request.data.get('type', '').split('.')[-1]
            
            if event_type == 'started':
                website_url.status = 'processing'
                website_url.metadata.update({
                    'crawl_started': True,
                    'crawl_id': request.data.get('id'),
                    'start_time': request.data.get('timestamp')
                })
                
            elif event_type == 'in_progress':
                # Process each page in the data array
                for page in request.data.get('data', []):
                    # Store the page content
                    if 'markdown' in page:
                        if not website_url.processed_content:
                            website_url.processed_content = page['markdown']
                        else:
                            website_url.processed_content += f"\n\n{page['markdown']}"
                    
                    # Update metadata with page information
                    if 'pages' not in website_url.metadata:
                        website_url.metadata['pages'] = []
                    
                    page_info = {
                        'url': page.get('metadata', {}).get('url'),
                        'title': page.get('metadata', {}).get('title'),
                        'timestamp': request.data.get('timestamp')
                    }
                    
                    # Add any warnings if present
                    if 'warning' in page:
                        page_info['warning'] = page['warning']
                    
                    website_url.metadata['pages'].append(page_info)
                
            elif event_type == 'completed':
                website_url.status = 'completed'
                website_url.metadata.update({
                    'crawl_completed': True,
                    'end_time': request.data.get('timestamp'),
                    'total_pages': len(website_url.metadata.get('pages', [])),
                    'final_status': 'success' if request.data.get('success') else 'failed'
                })
                
            elif event_type == 'error':
                website_url.status = 'failed'
                website_url.error_message = request.data.get('error', 'Unknown error occurred')
                website_url.metadata.update({
                    'error': request.data.get('error'),
                    'error_time': request.data.get('timestamp')
                })
            
            website_url.save()
            
            return Response({
                'message': f'Successfully processed {event_type} event',
                'url_id': url_id,
                'status': website_url.status
            }, status=status.HTTP_200_OK)
            
        except WebsiteURL.DoesNotExist:
            return Response(
                {'error': f'Website URL with id {url_id} not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
