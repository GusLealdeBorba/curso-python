from django.contrib import admin

from interno.models import Categoria, Produto


# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(    Produto, ProdutoAdmin)