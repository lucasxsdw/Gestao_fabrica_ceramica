from django.db import models

class funcionario(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome")
    funcao = models.CharField(max_length=255, verbose_name="Função")
    salario = models.DecimalField(decimal_places=2, max_digits=7, verbose_name="Salário")
    chave_pix = models.CharField(max_length=255, verbose_name="Chave pix")
    banco = models.CharField(max_length=255, verbose_name="Banco")

    def __str__(self):
        return self.nome

