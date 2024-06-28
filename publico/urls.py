from django.urls import path
from publico import views

urlpatterns = [
    path("clientes/cadastrar", views.cliente_cadastrar),
    path("clientes/", views.cliente_detalhe, name="cliente_detalhe"),
    path("contato/cadastrar/<int:id_cliente>", views.contato_cadastrar),
    path("contato/editar/<int:id>", views.contato_editar),
    path("contato/apagar/<int:id>", views.contato_apagar),
    path("contato/<int:id>", views.contato_detalhe),

    path("endereco/cadastrar/<int:id_cliente>", views.endereco_cadastrar),
    path("endereco/editar/<int:id>", views.endereco_editar),
    path("endereco/apagar/<int:id>", views.endereco_apagar),


]