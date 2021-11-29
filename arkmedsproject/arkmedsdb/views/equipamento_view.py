from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.request import Request

from arkmedsdb.forms.decorator import form_validator

from arkmedsdb.helpers import(
    list_equipamentos_helper,
    get_equipamento_mais_chamados_helper
)

@api_view(['GET'])
def get_equipamento_mais_chamados(request):

    return get_equipamento_mais_chamados_helper()

@api_view(['GET'])
def list_equipamentos(request):
    
    return list_equipamentos_helper()