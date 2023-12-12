from django import forms
from .models import FAQ, FAQCategoria


class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['categoria', 'pergunta','descricao', 'resposta']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = FAQCategoria
        fields = ['nome']