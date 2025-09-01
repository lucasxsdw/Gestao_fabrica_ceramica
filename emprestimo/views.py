from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Emprestimo
from .forms import EmprestimoForm
from django.contrib import messages

from django.views.generic import ListView, DetailView, CreateView , UpdateView, DeleteView

class EmprestimoListView(ListView):
     model = Emprestimo
     template_name = 'emprestimo/listar.html'
     context_object_name = 'emprestimos'

class EmprestimoDetailView(DetailView):
    model = Emprestimo
    template_name = 'emprestimo/detalhar.html'
    context_object_name = 'emprestimo'
    
class EmprestimoCreateView(CreateView):
    model = Emprestimo
    form_class = EmprestimoForm
    template_name = 'emprestimo/form.html'
    success_url  = reverse_lazy('emprestimo:listar_emprestimos') 

class EmprestimoUpdateView(UpdateView):
    model = Emprestimo
    form_class = EmprestimoForm
    template_name = 'emprestimo/form.html'
    success_url  = reverse_lazy('emprestimo:listar_emprestimos') 

class EmprestimoDeleteView(DeleteView):
    model = Emprestimo
    template_name = 'confirmar_exclusao.html'
    success_url = reverse_lazy('emprestimo:listar_emprestimos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = self.success_url  # define the cancel URL
        return context