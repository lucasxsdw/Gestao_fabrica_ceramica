from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Material
from .forms import MaterialForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


class MaterialListView(ListView):
     model = Material 
     template_name = 'material/listar.html'
     context_object_name = 'materiais'


class MaterialAddView(CreateView):
    model = Material 
    form_class = MaterialForm
    template_name = 'material/form.html'
    success_url = reverse_lazy('material:listar_material')


class MaterialDetailView(DetailView):
    model = Material
    template_name = 'material/detalhar.html'
    context_object_name = 'material'
    

class MaterialUpdateView(UpdateView):
     model = Material
     form_class = MaterialForm
     template_name = 'material/form.html'
     success_url = reverse_lazy('material:listar_material')
     


class MaterialDeleteView(DeleteView):
    model = Material
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('material:listar_material')





@login_required
def obter_dias_emprestimo(request, id):
    material = get_object_or_404(Material, id=id)
    quantidade_dias = material.dias_de_emprestimo
    contexto = {'quantidade_dias': quantidade_dias}
    return JsonResponse(contexto)
