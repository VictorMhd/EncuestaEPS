from django.db.models import fields
from django.db.models.base import Model
from authApp.models.formulario import Formulario
from authApp.models.cedula import Cedula
from rest_framework import serializers

class FormularioSerializer (serializers.ModelSerializer):
    class Meta:
        Model = Formulario
        fields=['cedula_fk','identidad','temperatura','contacto',
                'diagnostico','dificultad','sintomas']