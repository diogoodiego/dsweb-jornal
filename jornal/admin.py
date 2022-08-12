from django.contrib import admin
from .models import Usuario, Edicao, Noticia, Comentario

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Edicao)
admin.site.register(Noticia)
admin.site.register(Comentario)