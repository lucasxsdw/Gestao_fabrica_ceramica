from django.urls import path
from . import views

from .views import (
    ProdutoListView,
    ProdutoDetailView,
    ProdutoCreateView,
    ProdutoUpdateView,
    ProdutoDeleteView
)

urlpatterns = [
    path('', ProdutoListView.as_view(), name='listar_produtos'),
    path('<int:pk>/', ProdutoDetailView.as_view(), name='detalhar_produto'),
    path('adicionar/', ProdutoCreateView.as_view(), name='adicionar_produto'),
    path('editar/<int:pk>/', ProdutoUpdateView.as_view(), name='editar_produto'),
    path('excluir/<int:pk>/', ProdutoDeleteView.as_view(), name='excluir_produto'),
]