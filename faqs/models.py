from django.db import models
from django.contrib.auth.models import User

class FAQCategoria(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
class FAQ(models.Model):
    categoria = models.ForeignKey(FAQCategoria, on_delete=models.CASCADE)
    pergunta = models.CharField(max_length=255)
    descricao = models.TextField()
    resposta = models.TextField(blank=True, null=True)
    def __str__(self) -> str:
          return f"Categoria: {self.categoria}, Pergunta: {self.pergunta}, Descrição: {self.descricao}, Resposta: {self.resposta}"
