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
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('funcionario:listar_funcionarios')







class FuncionarioDetailView(DetailView):
    model = Funcionario
    template_name = 'funcionario/detalhar_funcionario.html'
    context_object_name = 'funcionario'
    
