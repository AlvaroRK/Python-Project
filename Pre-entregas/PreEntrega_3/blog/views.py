from django.shortcuts import render, redirect
from .models import *
from .forms import CrearNuevoPost, CrearNuevaCategoria, CrearNuevoComentario
from django.http import HttpResponse

# Create your views here.


def index(request):
    title = "DJANGO COURSE"
    return render(request, "index.html", {
        'title': title
    })

# -------- COMENTARIOS ---------#


def comentarios(request):
    comentarios = Comentario.objects.all()
    return render(request, 'comentarios/comentarios.html', {
        'comentarios': comentarios
    })

# -------- CREAR COMENTARIOS ---------#


def crearComentario(request):
    if request.method == 'GET':
        return render(request, 'comentarios/crearComentarios.html', {
            'formComentario': CrearNuevoComentario()
        })
    else:
        print(request.POST)
        """ comment = request.POST['comentario']
        user = request.POST['nombreUsuario']
        post = request.POST['post_id']
        print(comment, user, post) """
        comentario = Comentario.objects.create(
            comentario=request.POST['comentario'],
            nombreUsuario_id=request.POST['nombreUsuario'],
            post_id = 30,
        )
        print(comentario)
        return render(request, 'comentarios/crearComentarios.html', {
            'formComentario': CrearNuevoComentario()
        })




# -------- CATEGORIAS ---------#
def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/categorias.html', {
        'categorias': categorias
    })

# -------- CREAR CATEGORIAS ---------#


def crearCategoria(request):
    if request.method == 'GET':
        return render(request, 'categorias/crearCategoria.html', {
            'formCategoria': CrearNuevaCategoria()
        })
    else:
        categoria = Categoria.objects.create(nombre=request.POST['nombre'])
        print(categoria)
        return render(request, 'categorias/crearCategoria.html', {
            'formCategoria': CrearNuevaCategoria()
        })


# -------- BUSCAR CATEGORIAS ---------#
# -------- FALTA ---------#





# -------- POST ---------#
def posts(request):
    comentarios = Comentario.objects.values()
    posts = Post.objects.all()
    return render(request, 'posts/posts.html', {
        'posts': posts,
        'comentarios': comentarios,
    })

# -------- CREAR POST ---------#


def crearPost(request):
    if request.method == 'GET':
        return render(request, 'posts/crearPost.html', {
            'formPost': CrearNuevoPost()
        })
    else:
        Post.objects.create(
            titulo=request.POST['titulo'],
            contenido=request.POST['contenido'],
            autor_id=1,
            categoria_id=request.POST['categoria']
        )
        return redirect("posts")

# -------- BUSCAR POST ---------#


def buscarPost(request):
    categorias = []
    for categoria in Categoria.objects.values():
        categorias.append(categoria)
    return render(request, 'posts/buscarPost.html', {
        'categorias': categorias
    })


def buscar(request):
    if request.method == 'GET':
        """ categoria = request.GET['categoria']
        print(categoria)
        categorias = Post.objects.filter(categoria_id__icontains=1) """
        titulo = request.GET['titulo']
        titulos = Post.objects.filter(titulo__icontains=titulo)

        return render(request, 'posts/resultadoBusqueda.html', {
            'titulo': titulo,
            'titulos': titulos,
            # 'categoria':categoria,
            # 'categorias':categorias,
        })
    else:
        respuesta = 'no se encontraron los datos'
    return HttpResponse(respuesta)
