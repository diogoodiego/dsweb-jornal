from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Usuario, Noticia, Edicao, Comentario
from django.utils import timezone
from .forms import UsuarioForm, LoginForm


def index(request):
    noticias = Noticia.objects.order_by('-data_hora')
    contexto = {"user":request.user, "noticias":noticias}
    return render(request,"jornal/index.html",contexto)

class login_view(TemplateView):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('jornal:home')
            
        login_form = LoginForm
        contexto ={
            'login_form':login_form,
        }
        return render(request, 'jornal/login.html', contexto)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(request, username=login_form.data['username'], password=login_form.data['password'])
            if user is not None:
                print('here')
                login(request, user)
                return redirect('jornal:home')
            else:
                messages.error(request, 'Credenciais inválidas')
        contexto ={
            'login_form':login_form,
        }
        return render(request, 'jornal/login.html', contexto)



class register_view(TemplateView):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('jornal:home')

        usuario_form = UsuarioForm
        contexto = {
            'usuario_form':usuario_form
        }
        return render(request,'jornal/register.html',contexto)

    def post(self, request):
        usuario_form = UsuarioForm(request.POST, request.FILES)
        if usuario_form.is_valid():
            user = User.objects.create_user(username=usuario_form.data['username'], email=usuario_form.data['email'], password=usuario_form.data['password'])
            user.save()
            usuario = Usuario(
                user = user,
                tipo=usuario_form.data['tipo'],
                imagem=usuario_form.files['imagem'],
            )
            usuario.save()
            return redirect('jornal:login')

        contexto = {
            'usuario_form':usuario_form
        }
        return render(request,'jornal/register.html',contexto)

def logout_view(request):
    logout(request)
    return redirect('jornal:login')

class home(TemplateView):
    def get(self, request):
        if request.user.is_authenticated:
            noticias = Noticia.objects.order_by('-data_hora')
            contexto = {"user":request.user, "noticias":noticias}
            return render(request,"jornal/home.html",contexto)
        else:
            return redirect('jornal:login')

class noticia_view(TemplateView):
    def get(self, request):
        if request.user.is_authenticated:
            edicoes = Edicao.objects.all()
            contexto = {'edicoes': edicoes}
            return render(request, "jornal/noticia/create.html", contexto)
        else:
            return redirect('jornal:login')

    def post(self, request):
        titulo = request.POST['titulo']
        imagem = request.FILES['imagem']
        texto = request.POST['texto']
        edicao = get_object_or_404(Edicao, pk=request.POST['edicao'])
        data_hora = timezone.now()
        autor = request.user.usuario
        noticia = Noticia(titulo=titulo, imagem=imagem, edicao=edicao, data_hora=data_hora, autor=autor, texto=texto)
        noticia.save()

        return redirect('jornal:home')
        #return render(request, "jornal/noticia/create.html", {'msg':'Edicao = ' + edicao})

class noticia_detalhe(TemplateView):
    def get(self, request,noticia_id):
        noticia = get_object_or_404(Noticia, pk=noticia_id)
        noticias = Noticia.objects.order_by('-data_hora')[:5]
        comentarios = Comentario.objects.filter(noticia=noticia_id)
        contexto = {"user":request.user, "noticia":noticia, "ultimas_noticias":noticias,"comentarios":comentarios}
        return render(request, "jornal/noticia/detalhe.html", contexto)

    def post(self, request, noticia_id):
        texto = request.POST['texto']
        data_hora = timezone.now()
        noticia = get_object_or_404(Noticia, pk=noticia_id)
        comentario = Comentario(
            texto=texto,
            data_hora=data_hora,
            noticia=noticia,
            usuario=request.user.usuario
        )
        print("save")
        comentario.save()
        return redirect('jornal:noticia_detalhe',noticia_id)


class test_view(TemplateView):
    def get(self,request):
        return render(request,"jornal/test.html")
        
    def post(self, request):
        item = request.POST.getlist('item')
        print(item)
        return redirect("jornal:test")
