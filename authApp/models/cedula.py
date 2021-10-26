from django.db import models

class Cedula(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Cedula', max_length=50)