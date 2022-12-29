from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile

class UserUpdateForm(ModelForm):
    email = forms.EmailField(max_length="100")
    
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']