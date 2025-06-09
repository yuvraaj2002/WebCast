from django.urls import path
from .views import URLProcessView, FirecrawlWebhookView

urlpatterns = [
    path('process-url/', URLProcessView.as_view(), name='process-url'),
    path('webhook/', FirecrawlWebhookView.as_view(), name='firecrawl-webhook'),
]