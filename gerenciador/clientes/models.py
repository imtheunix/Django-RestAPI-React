from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    mensagem = models.CharField(max_length=500, blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    