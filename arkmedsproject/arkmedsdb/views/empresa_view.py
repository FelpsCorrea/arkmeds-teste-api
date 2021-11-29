from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_401_UNAUTHORIZED,
    HTTP_500_INTERNAL_SERVER_ERROR
)
from arkmedsdb.forms.decorator import form_validator

from arkmedsdb.helpers import(
    list_empresas_helper,
    get_empresa_mais_equipamentos_helper
)

@api_view(['GET'])
def get_empresa_mais_equipamentos(request):

    return get_empresa_mais_equipamentos_helper()

@api_view(['GET'])
def list_empresas(request):
    
    return list_empresas_helper()