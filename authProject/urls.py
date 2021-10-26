"""epsProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views
urlpatterns = [
    path('login/', TokenObtainPairView.as_view()), #iniciar sesión
    path('refresh/', TokenRefreshView.as_view()), #refrescar el token
    path('user/', views.UserCreateView.as_view()), #crea nuevo usuario
    path('formulario/', views.FormularioCreateView.as_view()), #registrar una nueva postulación
    path('cedula/', views.allCedulaView.as_view())

]
