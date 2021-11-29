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

from arkmedsproject.settings import (
    ARKMEDS_DEV_TOKEN
)

from arkmedsdb.models import(
    Equipamento,
    Chamado
)

from arkmedsdb.serializers import(
    EquipamentoSerializer
)

def list_equipamentos_helper():

    try:

        equipamentos = Equipamento.objects.all()

        serializer = EquipamentoSerializer(equipamentos, many=True)

        response = serializer.data

        for equipamento in response:
            equipamento['count_chamados'] = Chamado.objects.filter(equipamento_id=equipamento['id']).count()

        return Response(
            {
                "status" : "Success",
                "message" : "Equipamentos encontrados com sucesso",
                "equipamentos": response
            }
        , status=HTTP_200_OK)
    
    except:
        return Response(
            {
                "status" : "Error",
                "message" : "Erro ao listar os equipamentos"
            }
        , status=HTTP_500_INTERNAL_SERVER_ERROR)

def get_equipamento_mais_chamados_helper():

    try:

        chamados = Chamado.objects.values('equipamento_id').annotate(chamados_count=Count('equipamento_id')).order_by('-chamados_count')

        equipamento = Equipamento.objects.get(pk=chamados[0]['equipamento_id'] if len(chamados)>0 else 0)

        serializer = EquipamentoSerializer(equipamento, fields=('id', 'modelo', 'numero_serie', 'id_ref', 'proprietario'))

        response = serializer.data

        response['count_chamados'] = chamados[0]['chamados_count']


        return Response(
            {
                "status" : "Success",
                "message" : "Equipamento com mais chamados encontrado",
                "equipamento": response
            }
        , status=HTTP_200_OK)

    except ObjectDoesNotExist:
        return Response(
            {
                "status" : "Success",
                "message" : "Não foram encontrados equipamentos"
            }
        , status=HTTP_404_NOT_FOUND)

    except:
        return Response(
            {
                "status" : "Error",
                "message" : "Erro ao encontrar o equipamento com mais chamados"
            }
        , status=HTTP_500_INTERNAL_SERVER_ERROR)
