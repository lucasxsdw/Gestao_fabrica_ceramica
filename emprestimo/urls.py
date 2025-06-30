from django.urls import path
from . import views

app_name = 'emprestimo'

urlpatterns = [
    path('', views.listar, name='listar'),
    path('<int:id>', views.detalhar, name='detalhar'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('excluir/<int:id>', views.excluir, name='excluir'),
]