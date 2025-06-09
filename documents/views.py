from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from .models import UploadedDocument


class PDFUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        try:
            # Check if file is present in request
            if 'pdf_file' not in request.FILES:
                return Response(
                    {'error': 'No PDF file provided'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            pdf_file = request.FILES['pdf_file']
            
            # Validate file type
            if not pdf_file.name.endswith('.pdf'):
                return Response(
                    {'error': 'Only PDF files are allowed'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Create and save document with title, file type, and file size
            document = UploadedDocument(
                title=pdf_file.name,
                file_type='pdf',
                file_size=pdf_file.size,    
                page_count=pdf_file.page_count,
                uploaded_by=request.user
            )
            document.save()
            
            return Response({
                'message': 'PDF file uploaded successfully',
                'document_id': document.document_id,
                'title': document.title,
                'file_type': document.file_type,
                'file_size': document.file_size,
                'page_count': document.page_count,
                'uploaded_by': request.user.id
            }, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
