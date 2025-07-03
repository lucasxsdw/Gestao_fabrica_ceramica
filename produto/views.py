from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, ProducaoDiaria
from .forms import ProdutoForm, ProducaoDiariaForm

def listar(request):
    produtos = Produto.objects.all()
    return render(request, 'produto/listar.html', {'produtos': produtos})

def detalhar(request, id):
    produto = get_object_or_404(Produto, id=id)
    producoes = ProducaoDiaria.objects.filter(produto=id)
    contexto = {
        'produto': produto,
        'producoes': producoes
        }
    return render(request, 'produto/detalhar.html', contexto)

def adicionar(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produto/form.html', {'form': form})

def editar(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produto/form.html', {'form': form})

def excluir(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('listar_produtos')

""" 
def adicionar_producao(request):
    if request.method == 'POST':
        form = ProducaoDiariaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProducaoDiariaForm()
    return render(request, 'produto/form_producao.html', {'form': form})

def editar_producao(request, id):
    producao_diaria = get_object_or_404(ProducaoDiaria, id=id)
    if request.method == 'POST':
        form = ProducaoDiariaForm(request.POST, instance=producao_diaria)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProducaoDiariaForm(instance=producao_diaria)
    return render(request, 'produto/form.html', {'form': form}) """