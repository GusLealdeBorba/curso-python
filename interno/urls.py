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
    
]