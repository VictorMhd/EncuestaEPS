from django.db import models

from .cedula import Cedula

class Formulario(models.Model):
    id = models.AutoField(primary_key=True)
    cedula_fk=models.ForeignKey(Cedula,related_name='cedula_fk',on_delete=models.DO_NOTHING)
    identidad=models.IntegerField('Identidad')
    temperatura=models.BooleanField('temperatura')
    contacto=models.BooleanField('contacto')
    diagnostico=models.BooleanField('diagnostico')
    dificultad=models.BooleanField('dificultad')
    sintomas=models.BooleanField('sintomas')