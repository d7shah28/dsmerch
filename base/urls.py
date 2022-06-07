from urllib.parse import urlparse
from django.urls import path
from base import views

urlpatterns = [
    path('', views.test_page, name='test'),
]