
from django import forms
from .models import Funcionario



class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'
        widgets = {
            'data_admissao': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date'})
        }
        


    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')

        cpf = cpf.replace('.', '').replace('-', '')

        if not cpf.isdigit() or len(cpf) != 11:
            raise forms.ValidationError("CPF inválido. Deve conter 11 números.")

        return cpf

    def clean_contato(self):
        contato = self.cleaned_data.get('contato')

        contato = ''.join(filter(str.isdigit, contato))  

        if len(contato) != 11:
            raise forms.ValidationError("Número de telefone inválido. Deve conter 11 dígitos.")

        return contato


 
    

   