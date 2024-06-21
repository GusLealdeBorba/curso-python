from django.urls import path
from . import views



urlpatterns = [
    path("/", views.home, name="interno_home"), 
    path("/categoria", views.categoria_index, name="categorias"),
    path("/categoria/cadastrar", views.categoria_cadastrar),
    path("/categoria/apagar/<int:id>", views.categoria_apagar),
    path("/categoria/editar/<int:id>", views.categoria_editar),
    path("/categoria-form", views.categoria_form_index, name="categorias_form"),
    path("/categoria-form/cadastrar", views.categoria_form_cadastrar),
    path("/categoria-form/apagar/<int:id>", views.categoria_form_apagar),
    path("/categoria-form/editar/<int:id>", views.categoria_form_editar),
    path("/estado", views.estado_index, name="estados"),
    path("/estado/cadastrar", views.estado_cadastrar),
    path("/estado/editar/<int:id>", views.estado_editar),
    path("/estado/apagar/<int:id>", views.estado_apagar),
    path("/produto", views.produto_index, name="produtos"),
    path("/produto/cadastrar", views.produto_cadastrar),
    path("/produto/apagar/<int:id>", views.produto_apagar),
    path("/produto/editar/<int:id>", views.produto_editar),
    path("/cidade", views.cidade_index, name="cidades"),
    path("/cidade/cadastrar", views.cidade_cadastrar),
    path("/cidade/apagar/<int:id>", views.cidade_apagar),
    path("/cidade/editar/<int:id>", views.cidade_editar),

    
]