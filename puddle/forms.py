from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username  = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
        }))
    email  = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        'class': 'w-full py-4 px-6 rounded-xl'
        }))
    password1  = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'Password',
        'class': 'w-full py-4 px-6 rounded-xl'
        }))
    password2  = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'Confirm password',
        'class': 'w-full py-4 px-6 rounded-xl'
        }))