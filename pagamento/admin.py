from django.contrib import admin # importa o admin do django, para aparecer os models no painel de administração.
from .models import Pagamento # Importa o model Pagamento, que será registrado no admin.

@admin.register(Pagamento) # Decorador para registrar o model Pagamento no admin do Django.
class PagamentoAdmin(admin.ModelAdmin): # Classe que define como o model Pagamento será exibido no painel de administração do Django.
    list_display = ('funcionario', 'data_pagamento', 'valor_total', 'vale_desconto', 'bonus_comissao') # Campos que serão exibidos na lista de pagamentos no admin.
    list_filter = ('data_pagamento', 'funcionario') # Campos que serão usados para filtrar os pagamentos no admin.
    search_fields = ('funcionario__nome',) # Campos que serão pesquisáveis no admin, permitindo buscar pagamentos pelo nome do funcionário.
