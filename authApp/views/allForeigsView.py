from _typeshed import Self
from django.conf import settings
from django.db.models.query import QuerySet
from rest_framework import generics, serializers, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.cedula import Cedula

from authApp.serializers.CedulaSerializers import CedulaSerializer

class allCedulaView(generics.ListAPIView):
    QuerySet = Cedula.objects.all()
    serializers_class = CedulaSerializer

    def get(self, request):
        return super().get(request)