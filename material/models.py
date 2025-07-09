from django.db import models
from funcionario.models import Funcionario
import datetime

class Material(models.Model):
    nome = models.CharField(max_length=100)
    certificado_aprovacao = models.IntegerField(verbose_name='Certificado de aprovação')
    dias_de_emprestimo = models.PositiveSmallIntegerField(verbose_name='Dias de empréstimo')
    fabricante = models.CharField(max_length=100, verbose_name='Fabricante')
    quantidade = models.PositiveIntegerField(verbose_name='Quantidade')
    funcionarios = models.ManyToManyField(Funcionario, through='emprestimo.Emprestimo')

    def __str__(self):
        return self.nome
    class Meta:
        permissions = [
        ('detail_material', 'Pode detalhar materiais'),
    ]
