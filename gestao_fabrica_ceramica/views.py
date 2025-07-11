from django.shortcuts import render
from django.db.models import Sum
from produto.models import Produto
from producao.models import Producao
from funcionario.models import Funcionario
from emprestimo.models import Emprestimo
from material.models import Material
from math import floor

def index(request):
    quantidade = 7 # quantidade de dias a consultar
    
    cont_funcionarios = Funcionario.objects.filter(status='Ativo').count()

    producao = Producao.objects.all()
    cont_producao = producao.aggregate(total=Sum('quantidade_produzida'))['total'] # contagem de todos os produtos produzidos
    contagem = max(producao.count(), 1) # usa 1 caso a contagem seja 0
    producao_media = floor(cont_producao / contagem) # média da contagem anterior

    producoes = producao.order_by('data')[:quantidade].values('data').annotate(total=Sum('quantidade_produzida')) # calcula a produção total de cada dia dentro de um perído

    for p in producoes:
        p['data'] = p['data'].strftime("%d/%m")

    producoes_por_produto = producao[:quantidade].values('produto__nome').annotate(total=Sum('quantidade_produzida'))

    cont_emprestimos = Emprestimo.objects.filter(status='Pendente').count()

    cont_materiais = Material.objects.aggregate(total=Sum('quantidade'))['total']

    contexto = {
        'cont_funcionarios': cont_funcionarios,
        'producao_media': producao_media,
        'cont_producao': cont_producao,
        'producoes': list(producoes),
        'producoes_por_produto': list(producoes_por_produto),
        'quantidade': quantidade,
        'cont_emprestimos': cont_emprestimos,
        'cont_materiais': cont_materiais
    }

    return render(request, 'index.html', contexto)