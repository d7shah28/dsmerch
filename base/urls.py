from urllib.parse import urlparse
from django.urls import path
from base import views

urlpatterns = [
    path('', views.products_list, name='home'),
    path('register/', views.register, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('products/<int:pk>/', views.product_detail, name="product"),
    path('staff/products/', views.staff_products_list, name='staff-products-view'),
]