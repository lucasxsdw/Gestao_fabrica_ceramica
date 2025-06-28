from django.db import models #trás todos os tipos de campos que será usado(CharField, DateField, DecimalField, etc.)
from funcionario.models import Funcionario # Importa o model Funcionario, para criar um viculo ou relaciomento.

class Pagamento(models.Model): #
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='pagamentos')
    data_pagamento = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    vale_desconto = models.DecimalField(max_digits=10, decimal_places=2)
    bonus_comissao = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.funcionario.nome} - {self.data_pagamento} - R$ {self.valor_total}"