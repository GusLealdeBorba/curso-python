from django.shortcuts import render, redirect
from . import models

# Create your views here.

def produto_index(request):
    produtos = models.Produto.objects.all()
    contexto = {"produtos": produtos}
    return render(request, "produtos/index.html", context=contexto)


def produto_cadastrar(request):
       if request.method == "POST":
           nome = request.POST.get("nome")
           preco = request.POST.get("preco")
           id_categoria = request.POST.get("categoria")
           descricao = request.POST.get("descricao")
           produto = models.Produto(
               nome=nome,
               preco=preco,
               descricao=descricao,
               categoria_id=id_categoria,
           )
           produto.save()
           return redirect("produtos")
       categorias = models.Categoria.objects.all()
       contexto = {"categorias" : categorias}
       return render(request, "produtos/cadastrar.html", contexto)


def produto_editar(request, id= int):
   produto = models.Produto.objects.get(pk=id)

   if request.method == "POST":
        nome = request.POST.get("nome").capitalize()
        preco = request.POST.get("preco")
        id_categoria = request.POST.get("categoria")
        descricao = request.POST.get("descricao")
        produto.nome = nome
        produto.preco = preco
        produto.descricao = descricao
        produto.categoria_id = id_categoria
        produto.save()
        return redirect("produtos")
   
   categorias = models.Categoria.objects.order_by("nome").all()
   contexto = {
       "categorias": categorias,
       "produto": produto,
   }
   return render(request, "produtos/editar.html", contexto)


def produto_apagar(request, id= int):
    produto = models.Produto.objects.get(pk=id)
    produto.delete()
    return redirect("produtos")

