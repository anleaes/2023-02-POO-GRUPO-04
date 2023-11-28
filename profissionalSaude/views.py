from django.shortcuts import render

# Create your views here.

from .models import ProfissionalSaude
from rest_framework import viewsets
from .serializer import ProfissionalSaudeSerializer

# Após o comentario "# Create your views here." e crie as views "ProfissionalSaude".

class ProfissionalSaudeViewSet(viewsets.ModelViewSet):
    queryset = ProfissionalSaude.objects.all()
    serializer_class = ProfissionalSaudeSerializer  
