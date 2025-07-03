from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar, name='listar_produtos'),
    path('<int:id>', views.detalhar, name='detalhar_produto'),
    path('adicionar/', views.adicionar, name='adicionar_produto'),
    path('editar/<int:id>', views.editar, name='editar_produto'),
    path('excluir/<int:id>', views.excluir, name='excluir_produto'),
]