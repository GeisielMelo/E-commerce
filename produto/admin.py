from django.contrib import admin

from . import models
from .models import Produto, Variacao


class VariacaoInline(admin.TabularInline):
    model = models.Variacao
    extra = 1


class ProdutoAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'descricao_curta',
        'get_preco_formatado',
        'get_preco_promocional_formatado',
    ]
    inlines = [
        VariacaoInline
    ]


# Register your models here.
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Variacao)
