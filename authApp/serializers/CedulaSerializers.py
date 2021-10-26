from authApp.models.cedula import Cedula
from rest_framework import serializers
class CedulaSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        cedula = Cedula.objects.get(id=obj.id)
        return{
            'id':cedula.id,
            'nombre':cedula.nombre
        }
        