from urllib.parse import urlparse
from django.urls import path
from base import views

urlpatterns = [
    path('', views.test_page, name='test'),
    path('register/', views.register, name="register"),
    path('login/', views.login_page, name="login"),
]