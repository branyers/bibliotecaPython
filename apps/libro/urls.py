from django.urls import path
from.views import crearAutor,listaAutores,autoresLibros, editarAutor, eliminarAutor

urlpatterns = [
    path('crear_autor', crearAutor, name='crear_autor'),
    path('listar_autor',listaAutores, name='listar_autor'),
    path('lista_libros/<id>',autoresLibros, name='autores_libros'),
    path('editar_autor/<id>',editarAutor,name='editar_autor'),
    path('eliminar_autor/<id>', eliminarAutor, name='eliminar_autor')
]