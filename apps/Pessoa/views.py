from django.shortcuts import render

# Create your views here.

from .models import Pessoa
from rest_framework import viewsets
from .serializer import PessoaSerializer

# Após o comentario "# Create your views here." e crie as views "Pessoa".

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer  
