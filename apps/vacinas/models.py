from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Vacina(models.Model):
    nome = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    dose = models.IntegerField()

    class Meta:
        verbose_name = 'Vacina'
        verbose_name_plural = 'Vacinas'
        ordering =['id']
         
    def __str__(self):
        return self.nome