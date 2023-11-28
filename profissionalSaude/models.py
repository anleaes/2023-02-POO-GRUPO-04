from django.db import models

# Create your models here.

class ProfissionalSaude(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    registro = models.CharField(max_length=50)

    def __str__(self):
        return self.nome