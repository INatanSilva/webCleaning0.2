from django.db import models

# Create your models here.

class Request(models.Model):
    nome = models.CharField(max_length=255)
    numero_contato = models.CharField(max_length=255)
    tipo_limpeza = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nome} - {self.tipo_de_servico}"
