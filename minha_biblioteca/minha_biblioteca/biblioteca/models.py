from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Livro(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano_publicacao = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.titulo} por {self.autor}"

