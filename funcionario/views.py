from pyexpat.errors import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .models import Funcionario
from .forms import FuncionarioForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required  
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


class FuncionarioListView(ListView):
     model = Funcionario 
     template_name = 'funcionario/listar.html'
     context_object_name = 'funcionarios'

class FuncionarioAddView(CreateView):
    model = Funcionario 
    form_class = FuncionarioForm
    template_name = 'funcionario/form.html'
    success_url = reverse_lazy('funcionario:listar_funcionarios')

class FuncionarioUpdateView(UpdateView):
     model = Funcionario
     form_class = FuncionarioForm
     template_name = 'funcionario/form.html'
     success_url = reverse_lazy('funcionario:listar_funcionarios')

class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = 'confirmar_exclusao.html'
    success_url = reverse_lazy('funcionario:listar_funcionarios')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = self.success_url  # define the cancel URL
        return context

class FuncionarioDetailView(DetailView):
    model = Funcionario
    template_name = 'funcionario/detalhar.html'
    context_object_name = 'funcionario'
    