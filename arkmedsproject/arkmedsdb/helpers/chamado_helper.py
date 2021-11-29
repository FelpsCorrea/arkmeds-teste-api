from rest_framework.response import Response

from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_401_UNAUTHORIZED,
    HTTP_500_INTERNAL_SERVER_ERROR
)

from django.db.models import Count

from arkmedsdb.models import(
    Chamado
)

from arkmedsdb.serializers import(
    ChamadoSerializer
)

def list_chamados_helper():

    try:
        chamados = Chamado.objects.all()

        serializer = ChamadoSerializer(chamados, many=True)

        return Response(
            {
                "status" : "Success",
                "message" : "Chamados encontrados com sucesso",
                "chamados": serializer.data
            }
        , status=HTTP_200_OK)

    except:
        return Response(
            {
                "status" : "Error",
                "message" : "Erro ao encontrar os chamados"
            }
        , status=HTTP_500_INTERNAL_SERVER_ERROR)