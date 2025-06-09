from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Document(models.Model):
    document_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/%Y/%m/%d/')
    file_type = models.CharField(max_length=50, blank=True)
    file_size = models.BigIntegerField(help_text="File size in bytes")
    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='documents',
        verbose_name='Uploaded By'
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    # New fields for processed content
    processed_content = models.TextField(blank=True, null=True)
    metadata = models.JSONField(default=dict, blank=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['uploaded_by', 'created_at'])
        ]
    
    def __str__(self):
        return f"Document #{self.document_id} - {self.title} by {self.uploaded_by.username}"
    
    def process_document(self):
        """Process the document using PyMuPDF4LLM"""
        from .utils import PDFProcessor
        
        processor = PDFProcessor()
        result = processor.process_pdf(self.file.path)
        
        self.processed_content = result['markdown_text']
        self.metadata = result['metadata']
        self.save()
