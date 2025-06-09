from django.urls import path
from .views import URLProcessView

urlpatterns = [
    path('process-url/', URLProcessView.as_view(), name='process-url'),
]