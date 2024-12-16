from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm
# Create your views here.


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm  # Se você estiver usando um formulário personalizado
    template_name = 'home.html'
    success_url = reverse_lazy('home')  