from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Produto
from producao.models import Producao
from .forms import ProdutoForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

@login_required
@permission_required('produto.view_produto', raise_exception=True)
def listar(request):
    produtos = Produto.objects.all()
    return render(request, 'produto/listar.html', {'produtos': produtos})

@login_required
@permission_required('produto.detail_produto', raise_exception=True)
def detalhar(request, id):
    produto = get_object_or_404(Produto, id=id)
    producoes = Producao.objects.filter(produto=id).order_by('-data')
    contexto = {
        'produto': produto,
        'producoes': producoes
    }
    return render(request, 'produto/detalhar.html', contexto)

@login_required
@permission_required('produto.add_produto', raise_exception=True)
def adicionar(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto adicionado com sucesso!")
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produto/form.html', {'form': form})

@login_required
@permission_required('produto.change_produto', raise_exception=True)
def editar(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto editado com sucesso!")
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produto/form.html', {'form': form})

@login_required
@permission_required('produto.delete_produto', raise_exception=True)
def excluir(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    messages.success(request, "Produto excluído com sucesso!")
    return redirect('listar_produtos')