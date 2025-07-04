from django.db import models

class Produto(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=60)
    preco_unitario = models.DecimalField("Preço unitário", max_digits=6, decimal_places=2, null=True, blank=True)
    largura = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name="Largura (cm)")
    altura = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name="Altura (cm)")
    comprimento = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name="Comprimento (cm)")

    def __str__(self):
        return self.nome

class ProducaoDiaria(models.Model):
    data = models.DateField(verbose_name="Data da produção")
    quantidade_produzida = models.PositiveIntegerField(verbose_name="Quantidade produzida")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.data} - {self.produto.nome} "
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['data', 'produto'], name="unico_por_data")
        ]