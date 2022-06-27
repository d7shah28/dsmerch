from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import RegisterForm, LoginForm, DivErrorList
from .models import Product

def test_page(request):

    return render(request, 'base.html', {})

def register(request):

    if request.method == 'POST':
        form_class = RegisterForm(request.POST or None, error_class=DivErrorList)
        if form_class.is_valid():
            username = form_class.cleaned_data.get('username')
            email = form_class.cleaned_data.get('email')
            password = form_class.cleaned_data.get('password')

            user = User.objects.create_user(username, email, password)
            print("New user created:", user)
            if user:
                return redirect('login')
        else:
            print("ERROR")
    else:
        form_class = RegisterForm(error_class=DivErrorList)

    context = {
        "form": form_class
    }

    return render(request, 'auth/register.html', context)


def login_page(request):

    if request.method == 'POST':
        form_class = LoginForm(request.POST or None, error_class=DivErrorList)
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
    else:
        form_class = LoginForm(error_class=DivErrorList)
    context = {
        "form": form_class
    }
    return render(request, 'auth/login.html', context)


def logout_page(request):
    user = request.user
    if user:
        print("HI") 
        logout(request)
        return redirect('/')


def products_list(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'pages/products_list.html', context)


def product_detail(request, pk):
    product = Product.objects.get(_id=pk)
    countInStock = range(1, product.count_in_stock + 1)
    context = {
        "object": product,
        "countInStock": countInStock
    }

    return render(request, 'pages/product_detail.html', context)


def staff_products_list(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'staff/staff_products_list.html', context)


# CARD-BODY REDUCE PADDING
# STYLING OF EDIT ADDRESS PAGE
# Update Password change
