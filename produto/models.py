from django.db import models

class Produto(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=60)
    preco_unitario = models.DecimalField("Preço unitário", max_digits=6, decimal_places=2, null=True, blank=True)
    largura = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name="Largura (cm)")
    altura = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name="Altura (cm)")
    comprimento = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name="Comprimento (cm)")

    def __str__(self):
        return self.nome
    
    class Meta:
        permissions = [
        ('detail_produto', 'Pode detalhar produtos'),
    ]

    