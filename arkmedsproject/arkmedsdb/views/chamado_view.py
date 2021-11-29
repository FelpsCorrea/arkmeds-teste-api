from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.request import Request

from arkmedsdb.forms.decorator import form_validator

from arkmedsdb.helpers import(
    list_chamados_helper
)

@api_view(['GET'])
def list_chamados(request):
    
    return list_chamados_helper()