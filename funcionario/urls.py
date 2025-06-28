from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_funcionarios, name='listar_funcionarios'),              
    path('adicionar/', views.add_Func, name='adicionar_funcionario'),             
    path('editar/<int:id>/', views.editar_func, name='editar_funcionario'),     
    path('excluir/<int:id>/', views.excluir_func, name='excluir_funcionario'), 
    path('detalhes/<int:pk>/', views.detail_func, name='detalhes_funcionario'),   
]
