from django.contrib import admin
from .models import FAQCategoria, FAQ

@admin.register(FAQCategoria)
class FAQCategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)

@admin.register(FAQ)
class FAQCategoryAdmin(admin.ModelAdmin):
    list_display = ("categoria","pergunta","descricao","resposta")
