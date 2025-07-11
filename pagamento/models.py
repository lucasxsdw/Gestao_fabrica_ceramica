from django.db import models
from funcionario.models import Funcionario


class Pagamento(models.Model):
    funcionario = models.ForeignKey(
        Funcionario, on_delete=models.CASCADE, related_name='pagamentos')
    data_pagamento = models.DateField(verbose_name="Data de pagamento")
    vale_desconto = models.DecimalField(max_digits=10, decimal_places=2)
    bonus_comissao = models.DecimalField(max_digits=10, decimal_places=2)
    pago = models.BooleanField(default=False)

    @property
    def total_calculado(self):
        return self.funcionario.salario - self.vale_desconto + self.bonus_comissao

    def __str__(self):
        return f"{self.funcionario.nome} - {self.data_pagamento}"

    class Meta:
        permissions = [
            ('detail_pagamento', 'Pode detalhar um pagamento'),
        ]
