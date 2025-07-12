from django.db import models

class Funcionario(models.Model):

    FREQUENCIA_PAGAMENTO_CHOICES = [
        ('Semanal', 'Semanal'),
        ('Quinzenal', 'Quinzenal'),
        ('Mensal', 'Mensal'),
    ]

    STATUS_CHOICES = [
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo'),
        ('Férias', 'Férias'),
    ]

    TIPOS_CHAVES_PIX_CHOICES = [
    ('CPF', 'CPF'),
    ('TELEFONE', 'Telefone'),
    ('EMAIL', 'Email'),
    ('CHAVE_ALEATORIA', 'Chave Aleatória'),
]

    tipo_chave_pix = models.CharField(max_length=20,choices=TIPOS_CHAVES_PIX_CHOICES,   default='CPF', verbose_name="Tipo de chave Pix")
    chave_pix = models.CharField(max_length=255, verbose_name="Chave pix")

    nome = models.CharField(max_length=255, verbose_name="Nome")
    funcao = models.CharField(max_length=255, verbose_name="Função")
    salario = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Salário")

    banco = models.CharField(max_length=255, verbose_name="Banco")
    contato = models.CharField(max_length=20, verbose_name="Contato")
    cpf = models.CharField(max_length=14, verbose_name="CPF")
    data_admissao = models.DateField(verbose_name="Data de admissão")
    frequencia_pagamento = models.CharField(max_length=14,choices=FREQUENCIA_PAGAMENTO_CHOICES, verbose_name="Frequência de pagamento")
    status = models.CharField(max_length=10,choices=STATUS_CHOICES, verbose_name="Status")

    def __str__(self):
        return self.nome
    
    class Meta:
        permissions = [
        ('detail_funcionario', 'Pode detalhar funcionarios'),
    ]