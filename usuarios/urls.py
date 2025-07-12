from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('listar/', views.listar, name='listar_usuarios'),
    path('editar/<int:id>/', views.editar, name='editar_usuario'),
    path('excluir/<int:id>/', views.excluir, name='excluir_usuario'),
]
