from tabnanny import verbose
from django.db import models

# Create your models here.
#Una vez creado el modelo se tiene que usar el comando de consola para aplicar los cambios a la base de datos
#pipenv run python3 manage.py makemigrations

#Seguido del comando para aplicar esos cambios
#pipenv run python3 manage.py migrate

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")

    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"

    def __str__(self):
        return self.title
