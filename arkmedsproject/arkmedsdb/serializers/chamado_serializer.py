from rest_framework import serializers

from .dynamic_serializer import DynamicFieldsModelSerializer

from . import(
    EquipamentoSerializer
)

from arkmedsdb.models import(
    Chamado
)

'''
	Classe para serializar o Chamado
'''
class ChamadoSerializer(DynamicFieldsModelSerializer):

    equipamento = EquipamentoSerializer(many=False, fields=('id', 'tipo', 'fabricante', 'modelo', 'numero_serie', 'id_ref', 'proprietario'))

    class Meta:
        model = Chamado
        fields = '__all__'