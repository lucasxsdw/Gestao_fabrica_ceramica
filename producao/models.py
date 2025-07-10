from django.db import models
from produto.models import Produto

class Producao(models.Model):
    data = models.DateField(verbose_name="Data da produção")
    quantidade_produzida = models.PositiveIntegerField(verbose_name="Quantidade produzida")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.data} - {self.produto.nome} "
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['data', 'produto'], name="unico_por_data", violation_error_message="Já existe uma produção registrada para este produto nesta data.")
        ]
        permissions = [
        ('detail_producao', 'Pode detalhar produções'),
    ]
