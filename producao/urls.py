from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar, name='listar_producoes'),
    path('<int:id>', views.detalhar, name='detalhar_producao'),
    path('adicionar/', views.adicionar, name='adicionar_producao'),
    path('editar/<int:id>/', views.editar, name='editar_producao'),
    path('excluir/<int:id>/', views.excluir, name='excluir_producao'),
]