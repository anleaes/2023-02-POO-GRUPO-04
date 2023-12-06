from django.shortcuts import render

# Create your views here.
from .models import LocalVacinacao
from rest_framework import viewsets
from .serializer import LocalVacinacaoSerializer

class LocalVacinacaoViewSet(viewsets.ModelViewSet):
    queryset = LocalVacinacao.objects.all()
    serializer_class = LocalVacinacaoSerializer
