from django import forms

from publico.widgets import CustomFileImput, CustomSelect
from . import models 

class ClienteCadastroForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = ['nome', 'cpf', 'data_nascimento', 'email']


class ContatoCadastroForm(forms.ModelForm):
    class Meta:
        model = models.Contato
        fields = ["tipo", "valor"]
        widgets = {
            "valor": forms.TextInput(attrs={
                'class':'input',
            }),
            "tipo": forms.Select(attrs={
                'class' : 'select'
            })
        }

class ClienteEditarDetalheForm(forms.ModelForm):
    class Meta:
       model = models.Cliente
       fields = ["nome","rg","genero","foto_perfil"]
       widgets = {
            "nome": forms.TextInput(attrs={
                "class": "input"
            }),
            "rg": forms.TextInput(attrs={
                "class": "input"
            }),
            "genero": CustomSelect,
            "foto_perfil": CustomFileImput
        }       