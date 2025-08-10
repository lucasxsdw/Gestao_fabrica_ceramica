from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Emprestimo
from .forms import EmprestimoForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

from django.views.generic import ListView, DetailView, CreateView , UpdateView, DeleteView



class EmprestimoListView(ListView):
     model = Emprestimo
     template_name = 'emprestimo/listar_emprestimos.html'
     context_object_name = 'emprestimos'




class EmprestimoDetailView(DetailView):
    model = Emprestimo
    template_name = 'emprestimo/detail_emprestimo.html'
    context_object_name = 'emprestimo'
    




class EmprestimoCreateView(CreateView):
    model = Emprestimo
    form_class = EmprestimoForm
    template_name = 'emprestimo/add_emprestimos.html'
    success_url  = reverse_lazy('listar_emprestimos') 



class EmprestimoUpdateView(UpdateView):
    model = Emprestimo
    form_class = EmprestimoForm
    template_name = 'emprestimo/add_emprestimos.html'
    success_url  = reverse_lazy('listar_emprestimos') 


class EmprestimoDeleteView(DeleteView):
    model = Emprestimo
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('listar_emprestimos')



