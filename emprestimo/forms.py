from django import forms
from .models import Emprestimo

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = '__all__'
        widgets = {
            'data_emprestimo': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'data_devolucao': forms.DateInput(format='%Y-%m-%d', attrs={'disabled': True}),
        }