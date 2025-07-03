from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar, name='listar_materiais'),
    path('<int:id>', views.detalhar, name='detalhar_material'),
    path('adicionar/', views.adicionar, name='adicionar_material'),
    path('editar/<int:id>', views.editar, name='editar_material'),
    path('excluir/<int:id>', views.excluir, name='excluir_material'),
    path('<int:id>/quantidade_dias_emprestimo/', views.obter_dias_emprestimo)
]