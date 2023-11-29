from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'RegistroVacinação'

router = routers.DefaultRouter()
router.register('', views.RegistroVacinaçãoViewSet, basename='registroVacinacao')

urlpatterns = [
    path('', include(router.urls) )
]