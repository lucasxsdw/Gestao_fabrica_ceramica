from django.contrib import admin 
from .models import Pagamento 

@admin.register(Pagamento) 
class PagamentoAdmin(admin.ModelAdmin): 
    list_display = ('funcionario', 'data_pagamento', 'vale_desconto', 'bonus_comissao') 
    list_filter = ('data_pagamento', 'funcionario') 
    search_fields = ('funcionario__nome',) 
