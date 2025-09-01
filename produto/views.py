# produto/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages

from .models import Produto
from .forms import ProdutoForm
from producao.models import Producao  # só para mostrar produções no detalhe (opcional)


class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto/listar.html'
    context_object_name = 'produtos'

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto/detalhar.html'
    context_object_name = 'produto'

class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto/form.html'
    success_url = reverse_lazy('listar_produtos')

class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto/form.html'
    success_url = reverse_lazy('listar_produtos')

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'confirmar_exclusao.html'
    success_url = reverse_lazy('listar_produtos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = self.success_url  # define the cancel URL
        return context