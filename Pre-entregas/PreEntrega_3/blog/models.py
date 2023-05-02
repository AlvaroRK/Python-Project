from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre=models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fechaDePublicacion = models.DateTimeField(auto_now_add=True)
    imagenPortada = models.ImageField(null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    nombreUsuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.nombreUsuario} - {self.post}"