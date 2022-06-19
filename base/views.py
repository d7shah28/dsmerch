from math import prod
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import RegisterForm, LoginForm
from .models import Product

def test_page(request):

    return render(request, 'base.html', {})

def register(request):
    form_class = RegisterForm(request.POST or None)
    context = {
        "form": form_class
    }
    # print(request.POST)
    if form_class.is_valid():
        username = form_class.cleaned_data.get('username')
        email = form_class.cleaned_data.get('email')
        password = form_class.cleaned_data.get('password')

        user = User.objects.create_user(username,email,password)

        print("New user ", user)
    else:
        print("ERROR")
    return render(request, 'auth/register.html', context)


def login_page(request):
    form_class = LoginForm(request.POST or None)
    context = {
        "form": form_class
    }
    if form_class.is_valid():
        username = form_class.cleaned_data.get('username')
        email = form_class.cleaned_data.get('email')
        password = form_class.cleaned_data.get('password')

        user = authenticate(username=username, email=email, password=password)

        if user:
            login(request, user)
            return redirect('/')
    else:
        print("ERROR")
    return render(request, 'auth/login.html', context)

def logout_page(request):
    # user = request.user

    # if user: 
    #     logout(request)

    # return render(request, '')
    pass

def products_list(request):
    queryset = Product.objects.all()
    print(f"HIT HIT {request.user.is_authenticated}")
    context = {
        'object_list': queryset
    }
    return render(request, 'pages/products_list.html', context)


def product_detail(request, pk):
    product = Product.objects.get(_id=pk)

    context = {
        "object": product
    }

    return render(request, 'pages/product_detail.html', context)

# TODO INDIVIDUAL PRODUCT PAGE
# TODO LOGIN, REGISTER BORDER WITH SHADOW
# CARD-BODY REDUCE PADDING