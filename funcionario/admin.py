from django.contrib import admin
from .models import Funcionario

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome',)  # coloque os campos que quiser exibir
