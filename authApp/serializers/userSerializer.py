from authApp.models.user import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['id','password','nombre','apellido','email','celular']
    
    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        return {
            'nombre':user.nombre,
            'apellido': user.apellido,
            'email':user.email,
            'celular':user.celular  
        }