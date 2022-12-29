from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Post
from django.utils import timezone

class PostCreationForm(ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'image']

class SendEmailForm(forms.Form):
    first_name = forms.CharField(max_length=100, min_length=2)
    last_name = forms.CharField(max_length=100, min_length=2)
    email = forms.EmailField(max_length=250, min_length=2)
    employer = forms.CharField(max_length=100, min_length=2, required=False)
    job_title = forms.CharField(max_length=100, min_length=2, required=False)
    subject = forms.CharField(max_length=250)
    content = forms.CharField(min_length=1, widget=forms.Textarea)
