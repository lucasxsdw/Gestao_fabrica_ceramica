from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagamento_list, name='pagamento_list'),
    path('novo/', views.pagamento_create, name='pagamento_create'),
    path('<int:pk>/editar/', views.pagamento_update, name='pagamento_update'),
    path('<int:pk>/deletar/', views.pagamento_delete, name='pagamento_delete'),
]
