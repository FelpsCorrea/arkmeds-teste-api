from rest_framework import serializers

#Classe para importar os fields para serializar Dinâmicos
#O Serializer tem o argumento 'Fields' adicional

class DynamicFieldsModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):

        #Retira o argumento fields para passar para a superclasse
        fields = kwargs.pop('fields', None)

        super(DynamicFieldsModelSerializer, self).__init__(*args, *kwargs)

        if fields is not None:
            #Dropa qualquer field que não está especificado nos Fields
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)