from django.urls import path
from . import views 
from .views import FuncionarioListView, FuncionarioAddView, FuncionarioUpdateView, FuncionarioDeleteView, FuncionarioDetailView

app_name = 'funcionario'


urlpatterns = [
    path('', FuncionarioListView.as_view(), name='listar_funcionarios'),              
    path('adicionar/', FuncionarioAddView.as_view(), name='adicionar_funcionario'),             
    path('editar/<int:pk>/', FuncionarioUpdateView.as_view(), name='editar_funcionario'),     
    path('excluir/<int:pk>/', FuncionarioDeleteView.as_view(), name='excluir_funcionario'), 
    path('detalhes/<int:pk>/', FuncionarioDetailView.as_view(), name='detalhes_funcionario'),   
]


