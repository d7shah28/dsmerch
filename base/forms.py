from django import forms
from django.forms.utils import ErrorList


class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self: return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<div class="error alert alert-danger mt-1">%s</div>' % e for e in self])


class RegisterForm(forms.Form):
    username = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control my-2",
                    "placeholder": "Your username"
                }
            )
    )
    email = forms.EmailField(
            widget=forms.EmailInput(
                attrs={
                    "class": "form-control my-2",
                    "placeholder": "Your email"
                }
            )
    )
    password = forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    "class": "form-control my-2",
                    "placeholder": "Enter password..."
                }
            ))
    password2 = forms.CharField(label="Confirm Password", 
            widget=forms.PasswordInput(
                attrs={
                    "class": "form-control my-2",
                    "placeholder": "Confirm password..."
                }
    ))

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password2 != password:
            raise forms.ValidationError("Password should match.")
        return data


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control my-2",
                "placeholder": "Your Username"
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class":"form-control my-2",
                "placeholder":"Your email"
            }
        )
    )
    password = forms.CharField(label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control my-2",
                "placeholder":"Password"
            }
        )
    )