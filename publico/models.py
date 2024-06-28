from enum import Enum

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
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


class ClienteManager(BaseUserManager):
    def create_user(self, email, nome, cpf, data_nascimento, password=None, **extra_fields):
        if not email:
            raise ValueError('Email deve ser fornecido')
        email = self.normalize_email(email)
        user = self.model(
            email=email, nome=nome, cpf=cpf, data_nascimento=data_nascimento, **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, cpf, data_nascimento, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, nome, cpf, data_nascimento, password, **extra_fields)


# Create your models here.
class Cliente(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=260, unique=True)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    email = models.CharField(max_length=200, unique=True)
    rg = models.CharField(max_length=20, null=True)
    genero = models.CharField(choices=GeneroCliente.choices, null=True, max_length=40)
    foto_perfil = models.ImageField(upload_to="cliente_fotos_perfil", null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nome", "cpf", "data_nascimento"]

    objects = ClienteManager()

    def get_full_name(self):
        return self.nome

    def get_short_name(self):
        return self.nome

    def get_contatos(self):
        # SELECT com INNER JOIN
        return self.contato_set.all()

    def get_enderecos(self):
        return self.endereco_set.all()


class Contato(models.Model):
    tipo = models.CharField(choices=ContatoTipo.choices(), max_length=100)
    valor = models.CharField(max_length=200)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


class Endereco(models.Model):
    uf = models.CharField(max_length=2)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    numero = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)
    rua = models.CharField(max_length=100, null=True)
    complemento = models.TextField(null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
