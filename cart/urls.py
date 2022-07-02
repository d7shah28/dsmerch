from argparse import Namespace
from django.urls import path
from cart import views

urlpatterns = [
    path('', views.cart_home, name='cart_home'),
    path('update/', views.cart_update, name='cart_update'),
    path('checkout/',views.checkout_page, name='checkout'),
]