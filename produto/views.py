from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Produto
from producao.models import Producao
from .forms import ProdutoForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ProdutoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Produto
    template_name = 'produto/listar.html'
    context_object_name = 'produtos'
    permission_required = 'produto.view_produto'
    ordering = ['-id']


class ProdutoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Produto
    template_name = 'produto/detalhar.html'
    context_object_name = 'produto'
    permission_required = 'produto.view_produto'


class ProdutoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto/form.html'
    success_url = reverse_lazy('listar_produtos')
    permission_required = 'produto.add_produto'

    def form_valid(self, form):
        messages.success(self.request, 'Produto adicionado com sucesso!')
        return super().form_valid(form)


class ProdutoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto/form.html'
    success_url = reverse_lazy('listar_produtos')
    permission_required = 'produto.change_produto'

    def form_valid(self, form):
        messages.success(self.request, 'Produto editado com sucesso!')
        return super().form_valid(form)


class ProdutoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Produto
    template_name = 'confirm_delete.html'  
    success_url = reverse_lazy('listar_produtos')
    permission_required = 'produto.delete_produto'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Produto excluído com sucesso!')
        return super().delete(request, *args, **kwargs)