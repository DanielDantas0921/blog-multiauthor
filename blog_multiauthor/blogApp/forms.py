from django import forms
from .models import Post
from django_summernote.widgets import SummernoteWidget
from django_summernote.widgets import SummernoteInplaceWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'content', 'status', 'active']
        widgets = {
             'content': SummernoteWidget(),
        }
