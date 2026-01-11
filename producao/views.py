from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from produto.models import Produto
from .models import Producao
from .forms import ProducaoForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView



class ProducaoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Producao
    template_name = 'producao/listar.html'
    context_object_name = 'producoes'
    permission_required = 'producao.view_producao'

    def get_queryset(self):
        qs = super().get_queryset().order_by('-data')
        produto_id = self.request.GET.get('produto', None)
        data_inicial = self.request.GET.get('data_inicial', None)
        data_final = self.request.GET.get('data_final', None)

        if produto_id and produto_id != 'Todos':
            qs = qs.filter(produto__id=produto_id)
        if data_inicial:
            qs = qs.filter(data__gte=data_inicial)
        if data_final:
            qs = qs.filter(data__lte=data_final)

        return qs

    def render_to_response(self, context, **response_kwargs):
        if self.request.GET:
            producoes = self.get_queryset().values('id', 'produto__nome', 'quantidade_produzida', 'data')
            data_list = list(producoes)
            for p in data_list:
                p['data'] = p['data'].strftime("%d/%m/%Y")
            return JsonResponse(data_list, safe=False)
        else:
            context['produtos'] = Produto.objects.all()
            return super().render_to_response(context, **response_kwargs)


class ProducaoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Producao
    template_name = 'producao/detalhar.html'
    context_object_name = 'producao'
    permission_required = 'producao.detail_producao'


class ProducaoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Producao
    form_class = ProducaoForm
    template_name = 'producao/form.html'
    success_url = reverse_lazy('listar_producoes')
    permission_required = 'producao.add_producao'


class ProducaoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Producao
    form_class = ProducaoForm
    template_name = 'producao/form.html'
    success_url = reverse_lazy('listar_producoes')
    permission_required = 'producao.change_producao'


class ProducaoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Producao
    template_name = 'confirm_delete.html' 
    success_url = reverse_lazy('listar_producoes')
    permission_required = 'producao.delete_producao'
