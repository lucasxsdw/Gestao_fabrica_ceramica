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

    def __init__(self, *args, **kwargs):
        produto_obj = kwargs.pop("produto_obj", None)
        super().__init__(*args, **kwargs)

        if produto_obj:
            self.fields['produto'].queryset = Produto.objects.none()
            self.fields['produto'].initial = produto_obj.id
            self.fields['produto'].widget = forms.HiddenInput()

        if self.instance and self.instance.pk:
            self.fields['produto'].queryset = Produto.objects.filter(id=self.instance.produto.id)
            self.fields['produto'].initial = self.instance.produto.id
            self.fields['produto'].widget = forms.HiddenInput()
