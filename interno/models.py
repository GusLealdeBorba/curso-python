from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Estado(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    sigla = models.CharField(max_length=2, unique=True)


class Produto(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to="produtos_imagem", null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)


class Cidade(models.Model):
    nome = models.CharField(max_length=45, unique=True)
    quantidade = models.DecimalField(max_digits=40, decimal_places=6)
    clima = models.TextField(max_length=40)
    data = models.DateField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)





