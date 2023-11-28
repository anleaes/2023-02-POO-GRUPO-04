from django.db import models

# Create your models here.

class ProfissionalSaude(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    registro = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'ProfissionalSaude'
        verbose_name_plural = 'ProfissionaisSaude'
        ordering =['id']

    def __str__(self):
        return self.nome