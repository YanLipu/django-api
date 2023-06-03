from django.urls import path
from . import views

urlpatterns = [
    path('listar-usuarios', views.getUsuarios),
    path('listar-grupos', views.getGrupos)
]