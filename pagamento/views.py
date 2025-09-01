from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Pagamento
from .forms import PagamentoForm

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
    template_name = 'confirmar_exclusao.html'
    success_url = reverse_lazy('pagamento:listar_pagamentos')
    context_object_name = 'pagamento'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = self.success_url  # define the cancel URL
        return context

class PagamentoToggleView(View):
    def post(self, request, pk):
        pagamento = get_object_or_404(Pagamento, pk=pk)
        pagamento.pago = not pagamento.pago
        pagamento.save()
        messages.success(request, "Status do pagamento atualizado.")
        return redirect('pagamento:listar_pagamentos')
