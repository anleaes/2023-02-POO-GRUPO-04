from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'Pessoa'

router = routers.DefaultRouter()
router.register('', views.PessoaViewSet, basename='Pessoa')

urlpatterns = [
    path('', include(router.urls) )
]