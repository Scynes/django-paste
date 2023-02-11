from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    
    email = forms.EmailField(max_length=255, help_text='Required, as a valid email address!')