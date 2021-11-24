from django.db import models


# Create your models here.


class Autor(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    apellidos = models.CharField(max_length=100, blank=False, null=False)
    nacionalidad = models.CharField(max_length=100, blank=False, null=False)
    estado = models.BooleanField('Estado',default=True)
    descripcion = models.TextField(blank=False, null=False)
    fecha_creacion = models.DateField('Fecha de Creacion',auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        db_table = 'Autor'

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo',max_length=100, blank=False, null=False)
    fecha_publicacion = models.DateField('Fecha de Publicacion', blank=False, null=False)
    Autor = models.ManyToManyField(Autor,related_name="libros")

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        db_table = 'Libro'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo
