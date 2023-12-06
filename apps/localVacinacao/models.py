from django.db import models

# Create your models here.
class LocalVacinacao(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField()
    capacidade = models.IntegerField()

    def __str__(self):
        return self.nome