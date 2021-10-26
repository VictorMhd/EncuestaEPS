from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.formulario import Formulario
from authApp.serializers.FormularioSerializers import FormularioSerializer

class FormularioCreateView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = FormularioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
                
        return Response("formulario creado", status=status.HTTP_201_CREATED)