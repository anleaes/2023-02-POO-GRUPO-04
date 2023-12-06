from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'LocalVacinacao'

router = routers.DefaultRouter()
router.register('', views.LocalVacinacaoViewSet, basename='LocalVacinacao')

urlpatterns = [
    path('', include(router.urls) )
]