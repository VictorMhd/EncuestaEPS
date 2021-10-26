from django.contrib import admin
from .models.user import User
from .models.cedula import Cedula
from .models.formulario import Formulario

# Register your models here.
admin.site.register(User)
admin.site.register(Cedula)
admin.site.register(Formulario)