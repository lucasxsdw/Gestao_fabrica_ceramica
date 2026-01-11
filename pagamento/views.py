from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Pagamento
from .forms import PagamentoForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class PagamentoListView(ListView):
    model = Pagamento
    template_name = 'pagamento/listar.html'
    context_object_name = 'pagamentos'


class PagamentoDetailView(DetailView):
    model = Pagamento
    template_name = 'pagamento/detalhar.html'
    context_object_name = 'pagamento'


class PagamentoCreateView(CreateView):
    model = Pagamento
    form_class = PagamentoForm
    template_name = 'pagamento/form.html'
    success_url = reverse_lazy('pagamento:listar_pagamentos')


class PagamentoUpdateView(UpdateView):
    model = Pagamento
    form_class = PagamentoForm
    template_name = 'pagamento/form.html'
    success_url = reverse_lazy('pagamento:listar_pagamentos')


class PagamentoDeleteView(DeleteView):
    model = Pagamento
    template_name = 'confirm_delete.html'  # Pode usar template genérico
    success_url = reverse_lazy('pagamento:listar_pagamentos')

# refatorando dps
@login_required
# Alternar status (pago/não pago)
def pagamento_toggle(request, id):
    pagamento = get_object_or_404(Pagamento, id=id)
    pagamento.pago = not pagamento.pago
    pagamento.save()
    return redirect('pagamento:listar_pagamentos')
