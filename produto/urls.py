from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar, name='listar_produtos'),
    path('<int:id>', views.detalhar, name='detalhar_produto'),
    path('adicionar/', views.adicionar, name='adicionar_produto'),
    path('editar/<int:id>', views.editar, name='editar_produto'),
    path('excluir/<int:id>', views.excluir, name='excluir_produto'),

    path('<int:prod_id>/producao/adicionar/', views.adicionar_producao, name='adicionar-producao'),
    path('<int:prod_id>/producao/editar/<int:producao_id>/', views.editar_producao, name='editar-producao'),
    path('<int:prod_id>/producao/excluir/<int:producao_id>/', views.excluir_producao, name='excluir-producao'),
]