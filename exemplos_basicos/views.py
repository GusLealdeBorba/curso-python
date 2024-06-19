from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request) -> HttpResponse:
    response = HttpResponse(content="""
    {% load static %}
    <link rel="stylesheet" href="{% static 'exemplos_basicos/index.css' %}">
    <h1>Olá mundo</h1>                         
    <a href="contato">Contato</a>       
    <a href="/exemplos-basicos/jogo">Jogo</a> 
    <a href="/exemplos-basicos/calculadora">Calculadora</a>   
    <a href="/exemplos-basicos/sobre">Sobre</a>   
    <a href="/exemplos-basicos/calculadora-form">Calculadora-Form</a>
    <a href="/exemplos-basicos/sobre-form">Sobre-Form></a>
    <a href="/exemplos-basicos/carro-form>Carro-Form></a>
    <a href="/exemplos-basicos/carro-fm>Carro</a>
                 
    """)
    return response


def contato(request) -> HttpResponse:
    # Obteve o arquivo ontato.html e armazenou na variável template
    template = loader.get_template(template_name="contato.html")
    # Renderizar o template armazenando na variável html
    html = template.render(context={}, request=request)  
    response = HttpResponse(content=html)
    return response

def jogo(request) -> HttpResponse:
    return render(request, "jogo.html")


def calculadora(request, numero1: int = 3, numero2: int = 8) -> HttpResponse:
    # numero1 = 3
    # numero2 = 8
    soma = numero1 + numero2
    contexto_dados = {
        "n1": numero1,
        "n2": numero2,
        "soma": soma
    }
    return render(request, "calculadora.html", context=contexto_dados)


def calculadora_form(request):
    if request.method == "POST": 
        # Obter o query param (que está na URL)
        numero1 = int(request.POST.get("numero1"))
        numero2 = int(request.POST.get("numero2"))
        operacao = request.POST.get("operacao")

        match(operacao):
            case "somar": resultado = numero1 + numero2
            case "subtrair": resultado = numero1 - numero2
            case "multiplicar": resultado = numero1 * numero2
            case "dividir": resultado = numero1 / numero2
    else: 
        resultado : None

    return render(request, "calculadora-form.html", context={"resultado": resultado})


def calcular(request):
 # Obter o query param (que está na URL)
    numero1 = int(request.GET.get("numero1"))
    numero2 = int(request.GET.get("numero2"))
    operacao = request.GET.get("operacao")

    match(operacao):
        case "somar": resultado = numero1 + numero2
        case "subtrair": resultado = numero1 - numero2
        case "multiplicar": resultado = numero1 * numero2
        case "dividir": resultado = numero1 / numero2    
    
    return HttpResponse(f"Resultado: {resultado}")  

def sobre_form(request):
    return render(request, "sobre-form.html")


def sobre_fm(request):
    nome = request.GET.get("nome")
    sobrenome = request.GET.get("sobrenome")
    idade = int(request.GET.get("idade"))
    peso = float(request.GET.get("peso"))
    altura = float(request.GET.get("altura"))
    
    nome_completo = (nome + " " + sobrenome)
    nascimento = 2024 - idade 
    imc = peso / (altura * altura)
    sobre_dados = {
        "nm": nome, 
        "sbr": sobrenome,
        "ida": idade,
        "ps": peso, 
        "alt": altura,
        "nmc": nome_completo,
        "nasc": nascimento,
        "imc": imc
    }
    return render(request, "sobre.html", context=sobre_dados)

def carro_form(request):
    return render (request, "carro-form.html")


def carro_fm(request):
    modelo = request.POST.get("modelo")
    preco = float(request.POST.get("preco"))
    ano = request.POST.get("ano")
    cor = request.POST.get("cor")
    
    carro_dados = {
        "mdl": modelo,
        "prc": preco,
        "ano" : ano,
        "cor" : cor 
    }
    return render(request, "carro.html", context=carro_dados)

def sobre(request) -> HttpResponse:
    nome = "Gustavo"
    sobrenome = " Leal de Borba"
    nome_completo = nome + sobrenome
    idade = 15
    ano_nascimento = 2008
    peso = 70
    altura = 1.86
    imc = peso / (altura * altura)
    contexto_dados = {
        "nm":  nome,
        "sbr": sobrenome,
        "nc": nome_completo,
        "ida": idade,
        "ano": ano_nascimento,
        "ps": peso,
        "alt": altura,
        "im": imc
    }
    return render(request, "sobre.html", context=contexto_dados )


# Criar rota sobre com os seguintes dados no html
#   Nome (aluno escolhe o nome)
#   Sobrenome (aluno escolhe)
#   Nome completo (gerar o nome completo)
#   Idade (aluno escolhe)
#   Ano de Nascimento (gerar o ano nascimento)
#   Peso (aluno escolhe)
#   Altura (Aluno escolhe)
#   Imc (gerar o imc)
#   Imagem


# py manage.py runserver
# https://127.0.0.1:8000/exemplos-basicos/
