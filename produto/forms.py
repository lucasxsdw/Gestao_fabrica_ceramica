from django import forms
from .models import Produto, ProducaoDiaria

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

class ProducaoDiariaForm(forms.ModelForm):
    class Meta:
        model = ProducaoDiaria
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date'})
        }