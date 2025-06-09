from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Document

@receiver(post_save, sender=Document)
def process_document_on_upload(sender, instance, created, **kwargs):
    """Process document when it's first uploaded"""
    if created and instance.file:
        instance.process_document() 