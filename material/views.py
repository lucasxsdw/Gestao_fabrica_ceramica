from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages

from .models import Material
from .forms import MaterialForm


class MaterialListView(ListView):
    model = Material
    template_name = 'material/listar.html'
    context_object_name = 'materiais'
    paginate_by = 20  


class MaterialDetailView(DetailView):
    model = Material
    template_name = 'material/detalhar.html'
    context_object_name = 'material'


class MaterialCreateView(CreateView):
    model = Material
    form_class = MaterialForm
    template_name = 'material/form.html'
    success_url = reverse_lazy('listar_materiais')

class MaterialUpdateView(UpdateView):
    model = Material
    form_class = MaterialForm
    template_name = 'material/form.html'
    success_url = reverse_lazy('listar_materiais')

class MaterialDeleteView(DeleteView):
    model = Material
    template_name = 'confirmar_exclusao.html'
    success_url = reverse_lazy('listar_materiais')
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = self.success_url  # define the cancel URL
        return context

class MaterialLoanDaysView(View):
    """Retorna JSON com dias de empréstimo do material."""
    def get(self, request, pk):
        material = get_object_or_404(Material, pk=pk)
        return JsonResponse({'quantidade_dias': material.dias_de_emprestimo})
