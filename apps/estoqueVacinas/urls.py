from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'EstoqueVacinas'

router = routers.DefaultRouter()
router.register('', views.EstoqueVacinasViewSet, basename='EstoqueVacinas')

urlpatterns = [
    path('', include(router.urls) )]