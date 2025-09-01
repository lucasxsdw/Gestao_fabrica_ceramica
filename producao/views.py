from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from django.http import JsonResponse
from django.contrib import messages
from django.utils.dateparse import parse_date

from .models import Producao
from produto.models import Produto
from .forms import ProducaoForm


class ProducaoListView(ListView):
    model = Producao
    template_name = 'producao/listar.html'
    context_object_name = 'producoes'
    ordering = ['-data']

    def get_queryset(self):
        qs = super().get_queryset()
        produto_id = self.request.GET.get('produto')
        data_inicial = self.request.GET.get('data_inicial')
        data_final = self.request.GET.get('data_final')

        if produto_id and produto_id != 'Todos':
            qs = qs.filter(produto__id=produto_id)
        if data_inicial:
            di = parse_date(data_inicial)
            if di:
                qs = qs.filter(data__gte=di)
        if data_final:
            df = parse_date(data_final)
            if df:
                qs = qs.filter(data__lte=df)
        return qs

    def get(self, request, *args, **kwargs):
        # Se vieram filtros via GET, responde em JSON como no seu FBV
        if any(k in request.GET for k in ('produto', 'data_inicial', 'data_final')):
            qs = self.get_queryset().values('id', 'produto__nome', 'quantidade_produzida', 'data')
            data = []
            for p in qs:
                data.append({
                    'id': p['id'],
                    'produto__nome': p['produto__nome'],
                    'quantidade_produzida': p['quantidade_produzida'],
                    'data': p['data'].strftime('%d/%m/%Y') if p['data'] else None,
                })
            return JsonResponse(data, safe=False)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['produtos'] = Produto.objects.all()
        return ctx


class ProducaoDetailView(DetailView):
    model = Producao
    template_name = 'producao/detalhar.html'
    context_object_name = 'producao'


class ProducaoCreateView(CreateView):
    model = Producao
    form_class = ProducaoForm
    template_name = 'producao/form.html'
    success_url = reverse_lazy('listar_producoes')

class ProducaoUpdateView(UpdateView):
    model = Producao
    form_class = ProducaoForm
    template_name = 'producao/form.html'
    success_url = reverse_lazy('listar_producoes')

class ProducaoDeleteView(DeleteView):
    model = Producao
    template_name = 'confirmar_exclusao.html'
    success_url = reverse_lazy('listar_producoes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = self.success_url  # define the cancel URL
        return context