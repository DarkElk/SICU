from django.db import models
from django.utils import timezone


# class es una palabra clave que indica que estamos definiendo un objeto.
# Post es el nombre de nuestro modelo. Podemos darle un nombre diferente (pero debemos evitar espacios en blanco y caracteres especiales). Una clase siempre comienza con su primera letra en mayúscula.
# models.Model significa que Post es un modelo de Django, así Django sabe que debe guardarlo en la base de datos.
class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    link = models.TextField()
    fecha_creacion = models.DateTimeField(default = timezone.now)


#def significa que se trata de una función o método. publish es el nombre del método. Puedes cambiarlo, si quieres. La regla es que usamos minúsculas y guiones bajos en lugar de espacios
#(es decir, si quieres tener un método que calcule el precio medio, este podría llamarse calculate_average_price).
#esta parte a lo mejor no hace nada
def publicar(self):
    self.fecha_creacion = timezone.now()
    self.save()
#hasta acá
def __str__(self):
    return self.titulo
