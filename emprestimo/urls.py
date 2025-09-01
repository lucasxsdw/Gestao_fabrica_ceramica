from django.urls import path
from .views import (
    EmprestimoListView, EmprestimoDetailView, EmprestimoCreateView,
    EmprestimoUpdateView, EmprestimoDeleteView
)

app_name = 'emprestimo'

urlpatterns = [
    path('', EmprestimoListView.as_view(), name='listar_emprestimos'),
    path('<int:pk>/', EmprestimoDetailView.as_view(), name='detalhar_emprestimo'),
    path('novo/', EmprestimoCreateView.as_view(), name='adicionar_emprestimo'),
    path('<int:pk>/editar/', EmprestimoUpdateView.as_view(), name='editar_emprestimo'),
    path('<int:pk>/excluir/', EmprestimoDeleteView.as_view(), name='excluir_emprestimo'),
]
