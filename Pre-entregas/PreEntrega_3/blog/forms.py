from django import forms
from .models import Categoria, Post
from django.contrib.auth.models import User


"""-------------- POST --------------"""
lenCat = len(Categoria.objects.all())
CATEGORIAS_CHOICES = []
for category, i in zip(Categoria.objects.values(), range(1, lenCat+1)):
    CATEGORIAS_CHOICES.append((i, category['nombre']))
#print(CATEGORIAS_CHOICES)

class CrearNuevoPost(forms.Form):
    titulo = forms.CharField( max_length=40)
    contenido = forms.CharField(widget=forms.Textarea)
    categoria = forms.CharField(widget=forms.Select(choices=CATEGORIAS_CHOICES))


"""-------------- CATEGORIA --------------"""
class CrearNuevaCategoria(forms.Form):
    nombre = forms.CharField(label='Categoria', max_length= 30)


"""-------------- COMENTARIO --------------"""

lenUser= len(User.objects.all())
USER_CHOICES =[]
for user,i in zip(User.objects.values(), range(1, lenUser+1)):
    USER_CHOICES.append((i, user['username']))
#print(USER_CHOICES)

lenPost = len(Post.objects.all())
POST_CHOICES = []
for post,i in zip(Post.objects.values(), range(1, lenPost+1)):
    POST_CHOICES.append((i, post['titulo']))
#print(POST_CHOICES)


class CrearNuevoComentario(forms.Form):
    nombreUsuario = forms.CharField(widget=forms.Select(choices=USER_CHOICES), label='Nombre de usuario')
    comentario = forms.CharField(widget=forms.Textarea)
    post_id = forms.CharField(widget=forms.Select(choices=POST_CHOICES), label='Nombre del post')