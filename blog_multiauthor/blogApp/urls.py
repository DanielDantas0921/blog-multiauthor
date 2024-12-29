from django.urls import path
from .views import *

app_name = 'blogApp'
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path("postarPublicacao", PostCreateView.as_view(), name="postar"),
    path('listarPubliacoes', PostListView.as_view(), name="listar"),
    path('accounts/profile', testeAutenticacao.as_view(), name='loginPersonalizado')
]
