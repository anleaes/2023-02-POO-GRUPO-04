from django.shortcuts import render

# Create your views here.
from .models import EstoqueVacinas
from rest_framework import viewsets
from .serializer import EstoqueVacinasSerializer

class EstoqueVacinasViewSet(viewsets.ModelViewSet):
    queryset = EstoqueVacinas.objects.all()
    serializer_class = EstoqueVacinasSerializer