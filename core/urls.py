from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.lista_filmes, name='lista-filmes'),
    path('salvar/', views.salvar_filme, name='salvar'),
    path('excluir/<int:filme_id>/', views.excluir_filme, name='excluir'),
    path('atualizar/<int:filme_id>/', views.atualizar_filme, name='atualizar'),
]