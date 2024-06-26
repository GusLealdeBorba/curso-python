from enum import Enum
from django.db import models

class ContatoTipo(Enum): 
    EMAIL = "E-mail"
    CELULAR = "Celular"
    INSTAGRAM = "Instagram"
    @classmethod
    def choices(cls):
        return [(key.name, key.value) for key in cls]
    

class GeneroCliente(Enum):
    HOMEN = "Homen"
    MULHER = "Mulher"
    NAO_ESPECIFICADO = "Não especificado"
    @classmethod
    def choices(cls):
        return [(key.name, key.value) for key in cls]
    
    def get_contatos(self):
        # SELECT com INNER JOIN
        return self.contato_set.all()
# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=260, unique=True)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    email = models.CharField(max_length=200)
    rg = models.CharField(max_length=20, null=True)
    genero = models.CharField(choices=GeneroCliente.choices, null=True, max_length=40)
    foto_perfil = models.ImageField(upload_to="cliente_fotos_perfil", null=True)

    def get_contatos(self):
        # SELECT com INNER JOIN
        return self.contato_set.all()


class Contato(models.Model):
    tipo = models.CharField(choices=ContatoTipo.choices(), max_length=100)
    valor = models.CharField(max_length=200)
    cliente =  models.ForeignKey(Cliente, on_delete=models.CASCADE)


class Endereco(models.Model):
    uf = models.CharField(max_length=2)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    numero = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)