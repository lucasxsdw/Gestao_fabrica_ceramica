from django.urls import path
from .views import (MaterialListView, MaterialDetailView, MaterialCreateView, MaterialUpdateView, MaterialDeleteView, MaterialLoanDaysView,)

urlpatterns = [
    path('', MaterialListView.as_view(), name='listar_materiais'),
    path('<int:pk>/', MaterialDetailView.as_view(), name='detalhar_material'),
    path('adicionar/', MaterialCreateView.as_view(), name='adicionar_material'),
    path('editar/<int:pk>/', MaterialUpdateView.as_view(), name='editar_material'),
    path('excluir/<int:pk>/', MaterialDeleteView.as_view(), name='excluir_material'),
    path('<int:pk>/quantidade_dias_emprestimo/', MaterialLoanDaysView.as_view(),
         name='quantidade_dias_emprestimo'),
]