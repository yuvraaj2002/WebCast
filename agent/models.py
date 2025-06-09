from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class WebsiteURL(models.Model):
    url_id = models.AutoField(primary_key=True)
    url = models.URLField(max_length=1000)
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
            models.Index(fields=['uploaded_by', 'created_at'])
        ]
    
    def __str__(self):
        return f"URL #{self.url_id} - {self.title} by {self.uploaded_by.username}"
