from django.urls import path
from . import views
from .views import EmprestimoListView, EmprestimoDetailView, EmprestimoCreateView, EmprestimoUpdateView, EmprestimoDeleteView


urlpatterns = [
    path('listar_emprestimos', EmprestimoListView.as_view(), name='listar_emprestimos'),
    path('<int:pk>', EmprestimoDetailView.as_view(), name='detalhar_emprestimo'),
    path('adicionar/', EmprestimoCreateView.as_view(), name='adicionar_emprestimo'),
    path('editar/<int:pk>', EmprestimoUpdateView.as_view(), name='editar_emprestimo'),
    path('excluir/<int:pk>', EmprestimoDeleteView.as_view(), name='excluir_emprestimo'),
]