from django.db import models

class Funcionario(models.Model):

    FREQUENCIA_PAGAMENTO_CHOICES = [
        ('SE', 'Semanal'),
        ('QI', 'Quinzenal'),
        ('ME', 'Mensal'),
    ]

    STATUS_CHOICES = [
        ('AT', 'Ativo'),
        ('IN', 'Inativo'),
        ('FA', 'Férias'),
    ]


    nome = models.CharField(max_length=255, verbose_name="Nome")
    funcao = models.CharField(max_length=255, verbose_name="Função")
    salario = models.DecimalField(decimal_places=2, max_digits=7, verbose_name="Salário")
    chave_pix = models.CharField(max_length=255, verbose_name="Chave pix")
    banco = models.CharField(max_length=255, verbose_name="Banco")
    contato = models.CharField(max_length=20, default='Sem contato',verbose_name="Contato")
    cpf = models.CharField(max_length=11, verbose_name="CPF")
    data_admissao = models.DateField(verbose_name="Data de admissão")
    frequencia_pagamento = models.CharField(max_length=20,choices=FREQUENCIA_PAGAMENTO_CHOICES, verbose_name="Frequência de pagamento")
    status = models.CharField(max_length=2,choices=STATUS_CHOICES, verbose_name="Status")


    def __str__(self):
        return self.nome