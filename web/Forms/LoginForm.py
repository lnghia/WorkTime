from django import forms
from django.core import validators

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    remember_me = forms.BooleanField(required=False)