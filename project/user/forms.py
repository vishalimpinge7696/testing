from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Signup
from django.contrib.auth.forms import UserCreationForm

class SignupForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the first name'
               }))

    photo = forms.ImageField(required=True, widget=forms.ImageField(
        attrs={'class': 'form-control', 'required': True, 'multiple': True, 'accept': 'image/*'}))

    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the E-mail ID'
               }))

    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the username'}))

    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the password'}))

    contact = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the Contact'}))

    class Meta:
        model = Signup
        fields = ('name', 'email', 'username', 'password', 'contact','cover')
