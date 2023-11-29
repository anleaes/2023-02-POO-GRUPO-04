from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    dose = models.IntegerField()

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering =['id']

    def str(self):
        return self.nome