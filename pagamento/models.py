from django.db import models #trás todos os tipos de campos que será usado(CharField, DateField, DecimalField, etc.)
from funcionario.models import Funcionario # Importa o model Funcionario, para criar um viculo ou relaciomento.

class Pagamento(models.Model): # Toda classe que herda de models.Model, vira uma tabela no banco de dados.
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='pagamentos') # Cria um relacionamento com o model Funcionario, onde cada pagamento está vinculado a um funcionário.
    data_pagamento = models.DateField(verbose_name= "Data de pagamento") # Campo para armazenar a data do pagamento.
    vale_desconto = models.DecimalField(max_digits=10, decimal_places=2) # Campo para armazenar o valor do vale desconto, com até 10 dígitos no total e 2 casas decimais.
    bonus_comissao = models.DecimalField(max_digits=10, decimal_places=2) # Campo para armazenar o valor do bônus ou comissão, com até 10 dígitos no total e 2 casas decimais.


    def __str__(self): # Método especial que o django usa para exibir o objeto como string(texto).
        return f"{self.funcionario.nome} - {self.data_pagamento} - R$ {self.valor_total}"