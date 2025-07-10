from django import forms
from .models import Producao

class ProducaoForm(forms.ModelForm):
    class Meta:
        model = Producao
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date'})
        }