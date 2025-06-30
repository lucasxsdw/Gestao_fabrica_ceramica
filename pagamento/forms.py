from django import forms
from .models import Pagamento

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['funcionario', 'data_pagamento', 'valor_total', 'vale_desconto', 'bonus_comissao']
