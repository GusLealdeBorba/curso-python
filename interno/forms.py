from django import forms
from . import models 

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = models.Categoria
        fields = ['nome']
        widgets = {
            "nome" : forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Ex. Ft'
            })
        }