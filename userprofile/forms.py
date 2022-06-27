from dataclasses import field
from email.policy import default
from turtle import width
from django import forms
from django.contrib.auth.models import User
from django.db import transaction
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField
from userprofile.models import ShippingAddress


class ProfileForm(forms.ModelForm):
    username = forms.CharField(label='Username',
        widget=forms.TextInput(
            attrs={
                "class":"form-control my-2"
            }
        )
    )
    email = forms.EmailField(label='Email',
        widget=forms.EmailInput(
            attrs={
                "class": "form-control my-2",
                "placeholder": "Your email"
            }
        )
    )
    first_name = forms.CharField(label='First Name (Optional)', 
        required=False,
        widget=forms.TextInput(
            attrs={
                "class":"form-control my-2",
                "placeholder":"First Name"
            }
        )
    )
    last_name = forms.CharField(label='Last Name (Optional)', 
        required=False,
        widget=forms.TextInput(
            attrs={
                "class":"form-control my-2",
                "placeholder":"Last Name"
            }
        )
    )
    password = forms.CharField(required=False,
            widget=forms.PasswordInput(
                attrs={
                    "class": "form-control my-2",
                    "placeholder": "Enter password..."
            }
        )
    )
    password2 = forms.CharField(label="Confirm Password",
            required=False, 
            widget=forms.PasswordInput(
                attrs={
                    "class": "form-control my-2",
                    "placeholder": "Confirm password..."
            }
        )
    )
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'password2',
        ]

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password2 != password:
            raise forms.ValidationError("Password should match.")
        return data

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get("email")
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        if self.cleaned_data.get("password") != "" or self.cleaned_data.get("password") is None:
            print("HIT")
            user.set_password(self.cleaned_data.get("password"))
        user.save()
        return user


class AddressForm(forms.ModelForm):
    name = forms.CharField(label='Address Name',
        widget=forms.TextInput(
            attrs={
                "class":"form-control my-2"
            }
        )
    )
    contact_number = forms.CharField(label='Contact Number',
        widget=forms.TextInput(
            attrs={
                "class":"form-control my-2"
            }
        )
    )
    address_line_1 = forms.CharField(label='Address Line 1',
        widget=forms.TextInput(
            attrs={
                "class":"form-control my-2"
            }
        )
    )
    address_line_2 = forms.CharField(label='Address Line 2',
        widget=forms.TextInput(
            attrs={
                "class":"form-control my-2"
            }
        )
    )
    city = forms.CharField(label='City Name',
        widget=forms.TextInput(
            attrs={
                "class":"form-control my-2"
            }
        )
    )
    state = forms.CharField(label='State Name',
        widget=forms.TextInput(
            attrs={
                "class":"form-control my-2"
            }
        )
    )
    pincode = forms.CharField(label='Pincode',
        widget=forms.TextInput(
            attrs={
                "class":"form-control my-2"
            }
        )
    )
    country = CountryField(blank_label='(Select Country)').formfield(
        widget=CountrySelectWidget
    )
    default = forms.BooleanField(label='Make Default Address?',
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-check"
            }
        )
    )
    
    class Meta:
        model = ShippingAddress
        fields = [
            'name',
            'contact_number',
            'address_line_1',
            'address_line_2',
            'city',
            'state',
            'pincode',
            'country',
            'default',
        ]