from django.urls import path
from . import views
from .views import (
    PagamentoListView,
    PagamentoDetailView,
    PagamentoCreateView,
    PagamentoUpdateView,
    PagamentoDeleteView,
)


app_name = 'pagamento'

urlpatterns = [
    path('', PagamentoListView.as_view(), name='listar_pagamentos'),
    path('adicionar/', PagamentoCreateView.as_view(), name='adicionar_pagamento'),
    path('<int:pk>/', PagamentoDetailView.as_view(), name='detalhar_pagamento'),
    path('editar/<int:pk>/', PagamentoUpdateView.as_view(), name='editar_pagamento'),
    path('excluir/<int:pk>/', PagamentoDeleteView.as_view(), name='excluir_pagamento'),

    path('toggle/<int:id>/', views.pagamento_toggle, name='pagamento_toggle'),
]
