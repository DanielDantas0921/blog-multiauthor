from django.urls import path
from .views import *


urlpatterns = [
    path("", PostCreateView.as_view(), name="home"),
]