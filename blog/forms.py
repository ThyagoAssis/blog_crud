from django import forms
from .models import Blog

class ImageForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'phtoto']
