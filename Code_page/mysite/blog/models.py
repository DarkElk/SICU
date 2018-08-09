from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# class es una palabra clave que indica que estamos definiendo un objeto.
# Post es el nombre de nuestro modelo. Podemos darle un nombre diferente (pero debemos evitar espacios en blanco y caracteres especiales). Una clase siempre comienza con su primera letra en mayúscula.
# models.Model significa que Post es un modelo de Django, así Django sabe que debe guardarlo en la base de datos.
@python_2_unicode_compatible
class Post(models.Model):
    autor = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    link = models.CharField(max_length=400)
    fecha_creacion = models.DateTimeField(default = timezone.now)
    #autor_Post = models.CharField(default = 'Camaleon anónimo' ,max_length = 20)

    def __str__(self):
        return self.titulo


class Usuarios_registrados(models.Model):
    nombre =            models.CharField(max_length=100)
    correo =            models.CharField(max_length=100)
    contraseña =        models.CharField(max_length=100)
    carrera =           models.CharField(max_length=100)
    fecha_creacion =    models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.nombre
