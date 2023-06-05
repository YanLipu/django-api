from django.urls import path
from . import views



urlpatterns = [
    path('listar-usuarios', views.UsuarioController.as_view()),
    path('listar-grupos', views.GrupoController.as_view()),
    path('criar-grupo', views.GrupoController.as_view()),
    path('editar-grupo/<int:id>', views.GrupoController.as_view()),
    path('excluir-grupo/<int:id>', views.GrupoController.as_view()),
    path('criar-usuario', views.UsuarioController.as_view()),
    path('editar-usuario/<int:id>', views.UsuarioController.as_view()),
    path('excluir-usuario/<int:id>', views.UsuarioController.as_view()),
]