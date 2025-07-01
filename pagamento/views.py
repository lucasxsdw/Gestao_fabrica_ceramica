from django.shortcuts import render, redirect, get_object_or_404
from .models import Pagamento
from .forms import PagamentoForm

# Listar todos os pagamentos
def listar(request):
    pagamentos = Pagamento.objects.all()
    return render(request, 'pagamento/listar.html', {'pagamentos': pagamentos})

# Detalhar um pagamento específico
def detalhar(request, id):
    pagamento = get_object_or_404(Pagamento, id=id)
    return render(request, 'pagamento/detalhar.html', {'pagamento': pagamento})

# Adicionar um novo pagamento
def adicionar(request):
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagamento:listar_pagamentos')
    else:
        form = PagamentoForm()
    return render(request, 'pagamento/form.html', {'form': form})

# Editar um pagamento
def editar(request, id):
    pagamento = get_object_or_404(Pagamento, id=id)
    if request.method == 'POST':
        form = PagamentoForm(request.POST, instance=pagamento)
        if form.is_valid():
            form.save()
            return redirect('pagamento:listar_pagamentos')
    else:
        form = PagamentoForm(instance=pagamento)
    return render(request, 'pagamento/form.html', {'form': form})

# Excluir um pagamento
def excluir(request, id):
    pagamento = get_object_or_404(Pagamento, id=id)
    pagamento.delete()
    return redirect('pagamento:listar_pagamentos')

# Alternar status (pago/não pago)
def pagamento_toggle(request, id):
    pagamento = get_object_or_404(Pagamento, id=id)
    pagamento.pago = not pagamento.pago
    pagamento.save()
    return redirect('pagamento:listar_pagamentos')

