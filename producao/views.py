from django.shortcuts import render, redirect, get_object_or_404
from .models import Producao
from .forms import ProducaoForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

@permission_required('producao.view_producao', raise_exception=True)
@login_required
def listar(request):
    producoes = Producao.objects.all()
    return render(request, 'producao/listar.html', {'producoes': producoes})

@permission_required('producao.detail_producao', raise_exception=True)
@login_required
def detalhar(request, id):
    producao = get_object_or_404(Producao, id=id)
    return render(request, 'producao/detalhar.html', {'producao': producao})

@permission_required('producao.add_producao', raise_exception=True)
@login_required
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

@permission_required('producao.change_producao', raise_exception=True)
@login_required
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

@permission_required('producao.delete_producao', raise_exception=True)
@login_required
def excluir(request, id):
    producao = get_object_or_404(Producao, id=id)
    producao.delete()
    messages.success(request, 'Produção excluída com sucesso!')
    return redirect('listar_producoes')