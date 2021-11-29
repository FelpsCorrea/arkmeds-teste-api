from django.urls import path

from . import views

urlpatterns = [
    #External
    path('empresas-arkmeds', views.get_empresas_arkmeds),
    path('detalhe-empresa-arkmeds', views.get_detalhe_empresa_arkmeds),
    path('equipamentos-empresa-arkmeds', views.get_equipamentos_empresa_arkmeds),
    path('criar-chamado-equipamento-arkmeds', views.criar_chamado_equipamento_arkmeds),
    path('get-chamados-equipamento-arkmeds', views.get_chamados_equipamento_arkmeds),
    path('popular-banco', views.popular_banco),

    #Empresa
    path('get-empresa-mais-equipamentos', views.get_empresa_mais_equipamentos),
    path('list-empresas', views.list_empresas),

    #Equipamento
    path('get-equipamento-mais-chamados', views.get_equipamento_mais_chamados),
    path('list-equipamentos', views.list_equipamentos),

    #Chamado
    path('list-chamados', views.list_chamados)
]