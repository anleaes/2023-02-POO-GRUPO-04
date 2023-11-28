from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'Vacina'

router = routers.DefaultRouter()
router.register('', views.VacinaViewSet, basename='Vacina')

urlpatterns = [
    path('', include(router.urls) )
]