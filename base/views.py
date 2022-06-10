from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .forms import RegisterForm, LoginForm

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
            return redirect('/')
    else:
        print("ERROR")
    return render(request, 'auth/login.html', context)


# TODO Register,Login, Logout basic styling, Show products
    