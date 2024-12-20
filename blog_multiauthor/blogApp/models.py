from django.db import models
from django.contrib.auth.models import User
from django_summernote.fields import SummernoteTextField # type: ignore




# Create your models here.


class Post(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(default="Um teste de conteudo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True) # soft delete
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending') # aprovação para moderadores
    def __str__(self):
        return self.title