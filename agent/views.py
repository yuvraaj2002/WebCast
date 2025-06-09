from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import WebsiteURL
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

class URLProcessView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        try:
            # Get URL and title from request data
            url = request.data.get('url')
            title = request.data.get('title', '')
            
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
                title=title or url,  # Use URL as title if none provided
                url=url,
                uploaded_by=request.user
            )
            website_url.save()
            
            # Process the URL content
            website_url.process_url()
            
            return Response({
                'message': 'URL processed successfully',
                'url_id': website_url.url_id,
                'title': website_url.title,
                'url': website_url.url,
                'processed_content': website_url.processed_content,
                'metadata': website_url.metadata,
                'added_by': request.user.id
            }, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
