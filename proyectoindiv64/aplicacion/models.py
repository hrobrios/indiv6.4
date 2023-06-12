from django.db import models



class Usuarios(models.Model):
    nombre=models.CharField(max_length=20)
    clave=models.CharField(max_length=10)


def __str__(self):
    return self.nombre

def __str__(self):
    return self.clave

#se creó clave z1245678 y  user hernan dentro de admin