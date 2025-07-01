from django import forms
from .models import Pagamento

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['funcionario', 'data_pagamento','vale_desconto', 'bonus_comissao']
        widgets = {
            'data_pagamento': forms.DateInput(attrs={'type': 'date'}),
            'vale_desconto': forms.NumberInput(attrs={'step': '0.01'}),
            'bonus_comissao': forms.NumberInput(attrs={'step': '0.01'}),
        }