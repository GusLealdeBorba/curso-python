from enum import Enum
from django.db import models

class ContatoTipo(Enum): 
    EMAIL = "E-mail"
    CELULAR = "Celular"
    INSTAGRAM = "Instagram"
    @classmethod
    def choices(cls):
        return [(key.name, key.value) for key in cls]

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=260, unique=True)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    email = models.CharField(max_length=200)

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