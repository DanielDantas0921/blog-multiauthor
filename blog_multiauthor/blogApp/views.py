from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.utils.decorators import method_decorator
# Create your views here.

class HomeView(TemplateView):
    template_name = 'blogApp/home.html'

@method_decorator(xframe_options_exempt, name='dispatch')
class PostCreateView(CreateView , LoginRequiredMixin):
    model = Post
    form_class = PostForm  # Se você estiver usando um formulário personalizado
    template_name = 'blogApp/createPost.html'
    success_url = reverse_lazy('blogApp:home') 
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data 
    def post(self, request, *args, **kwargs):
        # Imprime os campos recebidos para depuração
        

        # Chama o método post original para processar o formulário
        content = request.POST.get('content', '')
        
        # Marcar como seguro para armazenar HTML no banco
        content_tratado= content.replace('"', "'")

        print("cleaned_tratado: abaixo")
        print(content_tratado)

        # Atualiza o POST para incluir o conteúdo tratado
        request.POST = request.POST.copy()
        request.POST['content'] = content_tratado

        
        # Chama o método post original
        return super().post(request, *args, **kwargs)

        # Retorna uma resposta JSON como exemplo
        if request.is_ajax():
            return JsonResponse({"message": "Dados recebidos com sucesso!"})
        return response


class PostListView(ListView):
    model = Post
    paginate_by = 10
    context_object_name = 'posts'
    template_name = 'blogApp/listPosts.html'

from allauth.socialaccount.adapter import get_adapter

class testeAutenticacao(TemplateView):
    template_name = 'blogApp/testeAutenticacao.html'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     adapter = get_adapter(self.request)
    #     context['social_providers'] = adapter.list_providers(self.request)
    #     print(str(context))
    #     return context
