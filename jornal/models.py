from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    USER_TIPOS = (
        ('L','Leitor'),
        ('E','Editor')
    )
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    tipo = models.CharField(max_length=1, choices=USER_TIPOS, null=True)
    imagem = models.ImageField(upload_to = 'autores', null = True)
    def __str__(self):
        return ("{0}").format(self.user)

class Edicao(models.Model):
    descricao = models.CharField(max_length=120)
    data_inicio = models.DateField(null=True)
    data_fim = models.DateField(null=True)
    def __str__(self):
        return ("{0} - {1}").format(self.descricao, self.data_fim)

class Noticia(models.Model):
    titulo = models.CharField(max_length=300)
    texto = models.TextField(null=True)
    imagem = models.ImageField(upload_to = 'noticias', null=True)
    edicao =  models.ForeignKey(Edicao, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(null=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    comentarios = models.ManyToManyField(Usuario, related_name = 'comentarios', through='Comentario')
    def __str__(self):
        return ("{0} - {1}").format(self.titulo, self.edicao.descricao)

class Comentario(models.Model):
    texto = models.CharField(max_length=800)
    data_hora = models.DateTimeField()
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return ("{0} - {1}").format(self.usuario.user.username, self.texto)



