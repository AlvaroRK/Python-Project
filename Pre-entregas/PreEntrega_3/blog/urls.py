from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name='index'),
    path("posts/", posts, name='posts'),
    path("crear_post/", crearPost, name='crear_post'),
    path("buscar_post/", buscarPost, name='buscar_post'),
    path("buscar/", buscar, name='buscar'),
    path("categorias/", categorias, name='categorias'),
    path("crear_categoria/", crearCategoria, name='crear_categoria'),
    path("comentarios/", comentarios, name='comentarios'),
    path("crear_comentario/", crearComentario, name='crear_comentario'),
]