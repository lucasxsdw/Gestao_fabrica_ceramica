from django.db import models
from funcionario.models import Funcionario
from material.models import Material
import datetime

class Emprestimo(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('pendente', 'Pendente'),
        ('devolvido', 'Devolvido')
    ]

    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(verbose_name='Data de empréstimo')
    data_devolucao = models.DateField(verbose_name='Data de devolução', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ativo', verbose_name='Status')

    def definir_data_devolucao(self):
        if self.material and self.data_emprestimo:
            self.data_devolucao = self.data_emprestimo + datetime.timedelta(days=self.material.dias_de_emprestimo)