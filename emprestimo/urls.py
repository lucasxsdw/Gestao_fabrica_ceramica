from django.urls import path
from . import views



urlpatterns = [
    path('', views.listar, name='listar_emprestimos'),
    path('<int:id>', views.detalhar, name='detalhar_emprestimo'),
    path('adicionar/', views.adicionar, name='adicionar_emprestimo'),
    path('editar/<int:id>', views.editar, name='editar_emprestimo'),
    path('excluir/<int:id>', views.excluir, name='excluir_emprestimo'),
]