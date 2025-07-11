from django.shortcuts import render, redirect, get_object_or_404
from produto.models import Produto
from .models import Producao
from .forms import ProducaoForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.http import JsonResponse

@login_required
@permission_required('producao.view_producao', raise_exception=True)
def listar(request):
    producoes = Producao.objects.all().order_by('-data')

    if request.GET:
        produto_id = request.GET.get('produto', None)
        data_inicial = request.GET.get('data_inicial', None)
        data_final = request.GET.get('data_final', None)

        if produto_id and produto_id != 'Todos':
            producoes = producoes.filter(produto__id=produto_id)
        if data_inicial:
            producoes = producoes.filter(data__gte=data_inicial)
        if data_final:
            producoes = producoes.filter(data__lte=data_final)

        #print(producoes.query)

        producoes = producoes.values('id', 'produto__nome', 'quantidade_produzida', 'data')

        for p in producoes:
            p['data'] = p['data'].strftime("%d/%m/%Y")

        return JsonResponse(list(producoes), safe=False)

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