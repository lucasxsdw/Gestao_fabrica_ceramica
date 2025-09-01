from django.urls import path
from .views import (ProducaoListView, ProducaoDetailView, ProducaoCreateView, ProducaoUpdateView, ProducaoDeleteView,)

urlpatterns = [
    path('', ProducaoListView.as_view(), name='listar_producoes'),
    path('novo/', ProducaoCreateView.as_view(), name='adicionar_producao'),
    path('<int:pk>/', ProducaoDetailView.as_view(), name='detalhar_producao'),
    path('<int:pk>/editar/', ProducaoUpdateView.as_view(), name='editar_producao'),
    path('<int:pk>/excluir/', ProducaoDeleteView.as_view(), name='excluir_producao'),
]
