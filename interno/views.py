from django.shortcuts import render, redirect

from interno.forms import CategoriaForm
from . import models

# Create your views here.

def home(request):
    return render(request, "home.html")

def categoria_index(request):
    # Consultar os registros da tabela de categorias (SELECT)
    categorias = models.Categoria.objects.all()
    contexto = {
        "categorias" : categorias
    }
    return render(
        request,
        "categorias/index.html",
        context=contexto,
    )


def categoria_cadastrar(request):
    if request.method == "GET":
        return render (request, "categorias/cadastrar.html")
    # Obtendo os dados que o usuáriuo preencheu nos campos
    nome = request.POST.get("nome").strip()
    # instancianddo um objeto da classe Categoria
    # preenchendo os atributos (nome)
    categoria = models.Categoria(nome=nome)
    # Executando a rotina de criar o registro da tabela de Categorias (INSERT INTO)
    categoria.save()
    # Redirencionar para a lista de caegorias (categoria_index)
    return redirect("categorias")


#   /categorio/apagar/<id>
def categoria_apagar(request, id: int):
    # Buscar a categoria que contém o id que veio na rota
    categoria = models.Categoria.objects.get(pk=id)
    # DELETE FROM categoria WHERE id = 2
    # Executar o delete na tabela de categoria filtrando por id
    categoria.delete()
    # Redireciona para a tela de listagem de categorias
    return redirect("categorias")

# /categoria/editar/<id>
def categoria_editar(request, id: int):
    categoria = models.Categoria.objects.get(pk=id)
    if request.method == "GET": 
        contexto = {"categoria": categoria}
        return render(request, "categorias/editar.html", context=contexto)
    
    categoria.nome = request.POST.get("nome").strip()
    categoria.save()
    return redirect("categorias")


def estado_index(request):
    estados = models.Estado.objects.all()
    contexto = {
        "estados" : estados
    } 
    print(contexto)
    return render(
        request,
        "estados/index.html",
        context=contexto
    )


def estado_cadastrar(request):
    if request.method == "GET":
        return render (request, "estados/cadastrar.html") 
    nome = request.POST.get("nome").strip()
    sigla = request.POST.get("sigla").strip()
    estado = models.Estado(nome=nome, sigla=sigla)
    estado.save()
    return redirect("estados")


def estado_editar(request, id: int):
    estado = models.Estado.objects.get(pk=id)
    if request.method == "GET":
        contexto = {"estado" : estado}
        return render(request, "estados/editar.html", context=contexto)
    
    estado.nome = request.POST.get("nome").strip()
    estado.sigla = request.POST.get("sigla").strip()
    estado.save()
    return redirect("estados")


def estado_apagar(request, id: int):
    estado = models.Estado.objects.get(pk=id)
    estado.delete()
    return redirect("estados")


def categoria_form_index(request):
    categorias = models.Categoria.objects.all()
    contexto = {
        "categorias" : categorias
    }
    return render(
        request,
        "categorias_forms/index.html",
        context=contexto,
    )


def categoria_form_cadastrar(request):
    # Verificado se a request é do tipo POST 
    if request.method == "POST":
        # construindo o form com os dados que o usuário preencheu
        form = CategoriaForm(request.POST)
        # valida se os dados preenchidos que estão no form são válidos 
        if form.is_valid():
            # Criar a categoria nesse caso 
            form.save()
            # Redirecionar para a linha de categorias
            return redirect("categorias_form")
        # Caso da requisição do tipo GET
    else:
        # Criando o form vazio
        form = CategoriaForm()
    # Criando o contexto passando o form
    contexto = {"form": form}
    # Retornnar o html do form 
    return render(request, "categorias_forms/cadastrar.html", context=contexto)


def categoria_form_editar(request, id: int):
    categoria = models.Categoria.objects.get(pk=id)
    if request.method == "POST": 
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect("categorias_form")
    else:
        form = CategoriaForm(instance=categoria)
    contexto = {
        "form": form,
        "categoria": categoria,
    }
    return render(request, "categorias_forms/editar.html", contexto)


def categoria_form_apagar(request, id: int):
    categoria = models.Categoria.objects.get(pk=id)
    categoria.delete()
    return redirect("categorias_form")


    