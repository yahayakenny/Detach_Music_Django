from django import forms
from band_app.models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'author','caption', 'description')