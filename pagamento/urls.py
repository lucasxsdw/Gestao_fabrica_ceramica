from django.urls import path
from .views import (PagamentoListView, PagamentoDetailView, PagamentoCreateView,PagamentoUpdateView, PagamentoDeleteView, PagamentoToggleView,)

app_name = 'pagamento'

urlpatterns = [
    path('', PagamentoListView.as_view(), name='listar_pagamentos'),
    path('<int:pk>/', PagamentoDetailView.as_view(), name='detalhar_pagamento'),
    path('adicionar/', PagamentoCreateView.as_view(), name='adicionar_pagamento'),
    path('editar/<int:pk>/', PagamentoUpdateView.as_view(), name='editar_pagamento'),
    path('excluir/<int:pk>/', PagamentoDeleteView.as_view(), name='excluir_pagamento'),
    path('toggle/<int:pk>/', PagamentoToggleView.as_view(), name='pagamento_toggle'),
]
