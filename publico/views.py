from django.shortcuts import get_object_or_404, redirect, render
from publico import models
from publico.form import ClienteCadastroForm, ClienteEditarDetalheForm, ContatoCadastroForm
from django.http import JsonResponse
from django.forms.models import model_to_dict

# Create your views here.
def cliente_cadastrar(request):
    if request.method == "POST":
        form = ClienteCadastroForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            return redirect("cliente_detalhe", id=cliente.id)
    
    form = ClienteCadastroForm()
    contexto = {"form": form}
    return render(request, "clientes/cadastrar.html", contexto)


def cliente_detalhe(request, id: int):
    cliente = get_object_or_404(models.Cliente, id=id)
    if request.method == "POST":
        form_cliente = ClienteEditarDetalheForm(request.POST, request.FILES, instance=cliente)
        if form_cliente.is_valid():
            form_cliente.save()

    contatos = cliente.get_contatos()
    
    form_cliente = ClienteEditarDetalheForm(instance=cliente)

    form_contato = ContatoCadastroForm()

    contexto = {"cliente": cliente, "contatos": contatos, "form_contato": form_contato, "form": form_cliente}
    return render(request, "clientes/detalhe.html", contexto)


def contato_cadastrar(request,id_cliente: int):
    # Consultar o cliente por id ou retornar um 404 para o cliete
    cliente = get_object_or_404(models.Cliente, id=id_cliente)
    # Construir o form do contato com os dados preenchidos na tabela
    form = ContatoCadastroForm(request.POST)
    # Construir o objeto de modelo.Contato, não persistindo os dados no banco de dados
    contato =form.save(commit=False) # Crinando o objeto do models.Contato
    # Vincular o cliente ao contato 
    contato.cliente = cliente
    # Persistir o contato no banco de dados
    contato.save()
    # Redirecionar para a tela de detalhe do cliente
    return redirect("cliente_detalhe", id=cliente.id)


def contato_editar(request, id: int):
    contato = get_object_or_404(models.Contato, id=id)
    form = ContatoCadastroForm(request.POST, instance=contato)
    contato = form.save()
    return redirect("cliente_detalhe", contato.cliente.id)


def contato_apagar(request, id: int):
    contato = get_object_or_404(models.Contato, id=id)
    id_cliente = contato.cliente.id
    contato.delete()
    return redirect("cliente_detalhe", id=id_cliente)


def contato_detalhe(request, id: int):
    contato = get_object_or_404(models.Contato, id=id)
    return JsonResponse(model_to_dict(contato))


def endereco_cadastrar(request):
    pass


def endereco_editar(request, id: int):
    pass


def endereco_apagar(request, id: int):
    pass

