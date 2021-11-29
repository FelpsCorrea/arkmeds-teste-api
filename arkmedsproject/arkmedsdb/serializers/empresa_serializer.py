from rest_framework import serializers

from .dynamic_serializer import DynamicFieldsModelSerializer

from arkmedsdb.models import(
    Empresa
)

'''
	Classe para serializar a Empresa
'''
class EmpresaSerializer(DynamicFieldsModelSerializer):

	class Meta:
		model = Empresa
		fields = '__all__'