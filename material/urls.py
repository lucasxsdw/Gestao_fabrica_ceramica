from django.urls import path
from . import views
from .views import MaterialListView, MaterialDetailView, MaterialAddView, MaterialUpdateView, MaterialDeleteView
app_name = 'material'


urlpatterns = [
    path('', MaterialListView.as_view(), name='listar_material'),
    path('adicionar/', MaterialAddView.as_view(), name='adicionar_material'),
    path('<int:pk>/', MaterialDetailView.as_view(), name='detalhar_material'),
    path('editar/<int:pk>/', MaterialUpdateView.as_view(), name='editar_material'),
    path('excluir/<int:pk>/', MaterialDeleteView.as_view(), name='excluir_material'),
    path('<int:id>/quantidade_dias_emprestimo/', views.obter_dias_emprestimo),

]