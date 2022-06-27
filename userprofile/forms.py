from msilib.schema import Error
from django import forms
from django.forms.utils import ErrorList
from django.contrib.auth.models import User


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
        widget=forms.TextInput(
            attrs={
                "class":"form-control my-2",
                "placeholder":"First Name"
            }
        )
    )
    last_name = forms.CharField(label='Last Name (Optional)',
        widget=forms.TextInput(
            attrs={
                "class":"form-control my-2",
                "placeholder":"Last Name"
            }
        )
    )
    password = forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    "class": "form-control my-2",
                    "placeholder": "Enter password..."
            }
        )
    )
    password2 = forms.CharField(label="Confirm Password", 
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
