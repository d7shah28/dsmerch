from django import forms
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

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            # 'password',
        ]