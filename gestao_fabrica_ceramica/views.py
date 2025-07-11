from django.shortcuts import render
from django.db.models import Sum
from produto.models import Produto
from producao.models import Producao
from funcionario.models import Funcionario
from math import floor

def index(request):
    quantidade = 30 # últimos 30 dias úteis
    
    cont_funcionarios = Funcionario.objects.filter(status='Ativo').count()

    producao = Producao.objects.all()[:quantidade]
    cont_producao = producao.aggregate(total=Sum('quantidade_produzida'))['total']
    producao_media = floor(cont_producao / quantidade)

    contexto = {
        'cont_funcionarios': cont_funcionarios,
        'producao_media': producao_media,
        'producao': producao,
    }

    return render(request, 'index.html', contexto)