from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_401_UNAUTHORIZED,
    HTTP_500_INTERNAL_SERVER_ERROR
)
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

from django.db.models import Count

from arkmedsdb.models import(
    Empresa,
    Equipamento
)

from arkmedsdb.serializers import(
    EmpresaSerializer
)

def list_empresas_helper():
    #try:

    empresas = Empresa.objects.all()

    serializer = EmpresaSerializer(empresas, many=True)

    response = serializer.data

    for empresa in response:
        empresa['count_equipamentos'] = Equipamento.objects.filter(proprietario_id=empresa['id']).count()

    return Response(
        {
            "status" : "Success",
            "message" : "Empresas encontrados com sucesso",
            "empresas": response
        }
    , status=HTTP_200_OK)
''' 
    except:
        return Response(
            {
                "status" : "Error",
                "message" : "Erro ao listar as empresas"
            }
        , status=HTTP_500_INTERNAL_SERVER_ERROR)
'''

def get_empresa_mais_equipamentos_helper():

    try:

        equipamentos = Equipamento.objects.values('proprietario_id').annotate(equipamentos_count=Count('proprietario_id')).order_by('-equipamentos_count')

        empresa = Empresa.objects.get(pk=equipamentos[0]['proprietario_id'] if len(equipamentos)>0 else 0)

        serializer = EmpresaSerializer(empresa, fields=('id', 'cnpj', 'nome', 'id_ref'))

        response = serializer.data

        response['count_equipamentos'] = equipamentos[0]['equipamentos_count']
        
        return Response(
            {
                "status" : "Success",
                "message" : "Empresa com mais equipamentos encontrada",
                "empresa": response
            }
        , status=HTTP_200_OK)

    except ObjectDoesNotExist:
        return Response(
            {
                "status" : "Success",
                "message" : "Não foram encontrados proprietários"
            }
        , status=HTTP_404_NOT_FOUND)

    except:
        return Response(
            {
                "status" : "Error",
                "message" : "Erro ao encontrar a empresa com mais equipamentos"
            }
        , status=HTTP_500_INTERNAL_SERVER_ERROR)