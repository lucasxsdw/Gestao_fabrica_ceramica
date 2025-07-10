from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Produto, ProducaoDiaria
from .forms import ProdutoForm, ProducaoDiariaForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages


@permission_required('produto.view_produto', raise_exception=True)
@login_required
def listar(request):
    produtos = Produto.objects.all()
    return render(request, 'produto/listar.html', {'produtos': produtos})

@permission_required('produto.detail_produto', raise_exception=True)
@login_required
def detalhar(request, id):
    produto = get_object_or_404(Produto, id=id)
    producoes = ProducaoDiaria.objects.filter(produto=id).order_by('-data')
    contexto = {
        'produto': produto,
        'producoes': producoes
    }
    return render(request, 'produto/detalhar.html', contexto)

@permission_required('produto.add_produto', raise_exception=True)
@login_required
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

@permission_required('produto.change_produto', raise_exception=True)
@login_required
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

@permission_required('produto.delete_produto', raise_exception=True)
@login_required
def excluir(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    messages.success(request, "Produto excluído com sucesso!")
    return redirect('listar_produtos')


@permission_required('produto.add_producao', raise_exception=True)
@login_required
def adicionar_producao(request, prod_id):
    produto = Produto.objects.get(id=prod_id)

    if request.method == 'POST':
        form = ProducaoDiariaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('detalhar_produto', kwargs={'id': prod_id}))
    else:
        form = ProducaoDiariaForm(produto_obj=produto)
    return render(request, 'produto/form_producao.html', {'form': form, 'produto': produto})

@permission_required('produto.change_producao', raise_exception=True)
@login_required
def editar_producao(request, prod_id, producao_id):
    producao_diaria = get_object_or_404(ProducaoDiaria, id=producao_id)
    produto = producao_diaria.produto

    if request.method == 'POST':
        form = ProducaoDiariaForm(request.POST, instance=producao_diaria)
        if form.is_valid():
            form.save()
            return redirect(reverse('detalhar_produto', kwargs={'id': prod_id}))
    else:
        form = ProducaoDiariaForm(instance=producao_diaria)
    return render(request, 'produto/form_producao.html', {'form': form, 'produto': produto})

@permission_required('produto.delete_producao', raise_exception=True)
@login_required
def excluir_producao(request, prod_id, producao_id):
    producao = get_object_or_404(ProducaoDiaria, id=producao_id)
    producao.delete()
    return redirect(reverse('detalhar_produto', kwargs={'id': prod_id}))