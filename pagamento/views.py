from django.shortcuts import render, redirect, get_object_or_404
from .models import Pagamento
from .forms import PagamentoForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages


@permission_required('pagamento.view_pagamento', raise_exception=True)
@login_required
# Listar todos os pagamentos
def listar(request):
    pagamentos = Pagamento.objects.all()
    return render(request, 'pagamento/listar.html', {'pagamentos': pagamentos})


@permission_required('pagamento.detail_pagamento', raise_exception=True)
@login_required
# Detalhar um pagamento específico
def detalhar(request, id):
    pagamento = get_object_or_404(Pagamento, id=id)
    return render(request, 'pagamento/detalhar.html', {'pagamento': pagamento})


@permission_required('pagamento.add_pagamento', raise_exception=True)
@login_required
# Adicionar um novo pagamento
def adicionar(request):
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Pagamento adicionado com sucesso!")
            return redirect('pagamento:listar_pagamentos')
    else:
        form = PagamentoForm()
    return render(request, 'pagamento/form.html', {'form': form})


@permission_required('pagamento.change_pagamento', raise_exception=True)
@login_required
# Editar um pagamento
def editar(request, id):
    pagamento = get_object_or_404(Pagamento, id=id)
    if request.method == 'POST':
        form = PagamentoForm(request.POST, instance=pagamento)
        if form.is_valid():
            form.save()
            messages.success(request, "Pagamento editado com sucesso!")
            return redirect('pagamento:listar_pagamentos')
    else:
        form = PagamentoForm(instance=pagamento)
    return render(request, 'pagamento/form.html', {'form': form})


@permission_required('pagamento.delete_pagamento', raise_exception=True)
@login_required
# Excluir um pagamento
def excluir(request, id):
    pagamento = get_object_or_404(Pagamento, id=id)
    pagamento.delete()
    messages.success(request, "Pagamento excluído com sucesso!")
    return redirect('pagamento:listar_pagamentos')


# refatorando dps
@login_required
# Alternar status (pago/não pago)
def pagamento_toggle(request, id):
    pagamento = get_object_or_404(Pagamento, id=id)
    pagamento.pago = not pagamento.pago
    pagamento.save()
    return redirect('pagamento:listar_pagamentos')
