from django import forms
from .models import Account


class LoginForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['email', 'password']