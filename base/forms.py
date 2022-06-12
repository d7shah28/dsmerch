from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your username"
                }
            )
    )
    email = forms.EmailField(
            widget=forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your email"
                }
            )
    )
    password = forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter password..."
                }
            ))
    password2 = forms.CharField(label="Confirm Password", 
            widget=forms.PasswordInput(
                attrs={
                    "class": "form-control",
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
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)