from django.shortcuts import render, redirect, get_object_or_404
from produto.models import Produto
from .models import Producao
from .forms import ProducaoForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

@login_required
@permission_required('producao.view_producao', raise_exception=True)
def listar(request):
    producoes = Producao.objects.all().order_by('-data')
    produtos = Produto.objects.all()
    contexto = {
        'producoes': producoes,
        'produtos': produtos,
    }
    return render(request, 'producao/listar.html', contexto)

@login_required
@permission_required('producao.detail_producao', raise_exception=True)
def detalhar(request, id):
    producao = get_object_or_404(Producao, id=id)
    return render(request, 'producao/detalhar.html', {'producao': producao})

@login_required
@permission_required('producao.add_producao', raise_exception=True)
def adicionar(request):
    if request.method == 'POST':
        form = ProducaoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produção adicionada com sucesso!')
            return redirect('listar_producoes')
    else:
        form = ProducaoForm()
    return render(request, 'producao/form.html', {'form': form})

@login_required
@permission_required('producao.change_producao', raise_exception=True)
def editar(request, id):
    producao = get_object_or_404(Producao, id=id)

    if request.method == 'POST':
        form = ProducaoForm(request.POST, instance=producao)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produção editada com sucesso!')
            return redirect('listar_producoes')
    else:
        form = ProducaoForm(instance=producao)
    return render(request, 'producao/form.html', {'form': form})

@login_required
@permission_required('producao.delete_producao', raise_exception=True)
def excluir(request, id):
    producao = get_object_or_404(Producao, id=id)
    producao.delete()
    messages.success(request, 'Produção excluída com sucesso!')
    return redirect('listar_producoes')