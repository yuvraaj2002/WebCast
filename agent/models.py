from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from urllib.parse import urlparse

class WebsiteURL(models.Model):
    PROCESSING_STATUS = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )

    url_id = models.AutoField(primary_key=True)
    url = models.URLField(max_length=1000)
    title = models.CharField(max_length=255, blank=True)  # Made blank=True as we'll set it in save()
    status = models.CharField(max_length=20, choices=PROCESSING_STATUS, default='pending')
    error_message = models.TextField(blank=True, null=True)
    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='website_urls',
        verbose_name='Added By'
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Fields for processed content
    processed_content = models.TextField(blank=True, null=True)
    metadata = models.JSONField(default=dict, blank=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['uploaded_by', 'created_at']),
            models.Index(fields=['status']),
        ]
    
    def __str__(self):
        return f"URL #{self.url_id} - {self.title} by {self.uploaded_by.username}"
    
    def save(self, *args, **kwargs):
        if not self.title:
            # Generate title from URL
            parsed_url = urlparse(self.url)
            self.title = parsed_url.netloc
        super().save(*args, **kwargs)
    
    def send_webhook_update(self, status, message=None, data=None):
        """Send webhook notification about processing status to the configured webhook URL"""
        from .tasks import send_webhook_notification
        send_webhook_notification.delay(
            settings.WEBHOOK_URL,
            {
                'url_id': self.url_id,
                'status': status,
                'message': message,
                'data': data
            }
        )
