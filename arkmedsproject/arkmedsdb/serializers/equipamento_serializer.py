from rest_framework import serializers

from .dynamic_serializer import DynamicFieldsModelSerializer

from . import(
	EmpresaSerializer
)

from arkmedsdb.models import(
    Equipamento
)

'''
	Classe para serializar o Equipamento
'''
class EquipamentoSerializer(DynamicFieldsModelSerializer):

	proprietario = EmpresaSerializer(many=False, fields=('id', 'nome', 'nome_fantasia', 'id_ref'))

	class Meta:
		model = Equipamento
		fields = '__all__'