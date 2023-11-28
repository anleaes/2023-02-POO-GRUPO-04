from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'profissionalSaude'

router = routers.DefaultRouter()
router.register('', views.ProfissionalSaudeViewSet, basename='profissionalSaude')

urlpatterns = [
    path('', include(router.urls) )
]