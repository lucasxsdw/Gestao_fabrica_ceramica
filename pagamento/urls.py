from django.urls import path
from . import views

app_name = 'pagamento'

urlpatterns = [
    path('', views.listar, name='listar_pagamentos'),
    path('<int:id>', views.detalhar, name='detalhar_pagamento'),
    path('adicionar/', views.adicionar, name='adicionar_pagamento'),
    path('editar/<int:id>', views.editar, name='editar_pagamento'),
    path('excluir/<int:id>', views.excluir, name='excluir_pagamento'),

    path('toggle/<int:id>/', views.pagamento_toggle, name='pagamento_toggle'),
]
