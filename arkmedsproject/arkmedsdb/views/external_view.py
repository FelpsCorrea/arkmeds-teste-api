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
    get_empresas_arkmeds_helper,
    get_detalhe_empresa_arkmeds_helper,
    get_equipamentos_empresa_arkmeds_helper,
    criar_chamado_equipamento_arkmeds_helper,
    get_chamados_equipamento_arkmeds_helper,
    popular_banco_helper
)

@api_view(['GET'])
def get_empresas_arkmeds(request):
    
    data = get_empresas_arkmeds_helper()

    if data['success']:
        return Response(
            {
                "status" : "Success",
                "message" : "Empresas da API Arkmeds listadas com sucesso",
                "empresas": data["response"]
            }
        , status=HTTP_200_OK)

    else:
        return Response(
            {
                "status" : "Error",
                "message" : "Erro ao listar as empresas da API Arkmeds"
            }
        , status=HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@form_validator(form_str={"GET":"GetDetalheEmpresasForm"})
def get_detalhe_empresa_arkmeds(request):
    
    params = request.query_params

    data = get_detalhe_empresa_arkmeds_helper(params['id_empresa'])

    if data['success']:
        return Response(
            {
                "status" : "Success",
                "message" : "Detalhe da empresa da API Arkmeds listado com sucesso",
                "detalhe": data["response"]
            }
        , status=HTTP_200_OK)

    else:
        return Response(
            {
                "status" : "Error",
                "message" : "Erro ao listar os detalhes da empresa"
            }
        , status=HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@form_validator(form_str={"GET":"GetDetalheEmpresasForm"})
def get_equipamentos_empresa_arkmeds(request):
    
    params = request.query_params

    data = get_equipamentos_empresa_arkmeds_helper(params['id_empresa'])

    if data['success']:
        return Response(
            {
                "status" : "Success",
                "message" : "Equipamentos da empresa da API Arkmeds listados com sucesso",
                "equipamentos": data["response"]
            }
        , status=HTTP_200_OK)

    else:
        return Response(
            {
                "status" : "Error",
                "message" : "Erro ao listar os equipamentos da empresa"
            }
        , status=HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@form_validator(form_str={"POST":"CriarChamadoEquipamentoForm"})
def criar_chamado_equipamento_arkmeds(request):
    
    params = request.data

    body = {
        "equipamento": params['id_equipamento'],
        "solicitante": params['id_solicitante'],
        "tipo_servico": params['tipo_servico'],
        "problema": params['problema'],
        "observacoes": params['observacoes'] if 'observacoes' in params else "",
        "data_criacao": params['data_criacao'],
        "id_tipo_ordem_servico": params['tipo_servico']
    }

    data = criar_chamado_equipamento_arkmeds_helper(body)

    if data['success']:
        return Response(
            {
                "status" : "Success",
                "message" : "Chamado criado com sucesso",
                "resposta": data["response"]
            }
        , status=HTTP_200_OK)

    else:
        return Response(
            {
                "status" : "Error",
                "message" : "Erro ao criar o chamado"
            }
        , status=HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@form_validator(form_str={"GET":"GetChamadosEquipamentoForm"})
def get_chamados_equipamento_arkmeds(request):
    
    params = request.query_params

    data = get_chamados_equipamento_arkmeds_helper(params['id_equipamento'])

    if data['success']:
        return Response(
            {
                "status" : "Success",
                "message" : "Chamados do equipamento da API Arkmeds listado com sucesso",
                "chamados": data["response"]
            }
        , status=HTTP_200_OK)

    else:
        return Response(
            {
                "status" : "Error",
                "message" : "Erro ao listar os chamados do equipamento"
            }
        , status=HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def popular_banco(request):
    
    try:
        popular_banco_helper()

        return Response(
            {
                "status" : "Success",
                "message" : "Banco populado com sucesso"
            }
        , status=HTTP_200_OK)

    except:
        return Response(
            {
                "status" : "Error",
                "message" : "Erro ao popular o banco"
            }
        , status=HTTP_500_INTERNAL_SERVER_ERROR)
        