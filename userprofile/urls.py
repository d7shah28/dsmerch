from django.urls import path
from userprofile import views

urlpatterns = [
    path('', views.profile_page, name='profile'),
    path('edit-address/<int:pk>/', views.edit_address, name='edit_address'),
]