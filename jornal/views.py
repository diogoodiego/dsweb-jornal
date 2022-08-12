from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Usuario, Noticia, Edicao
from django.utils import timezone
from .forms import UserForm, UsuarioForm


def index(request):
    return render(request,"jornal/index.html")

class login_view(TemplateView):
    def get(self, request):
        user_form = UserForm
        contexto ={
            'user_form':user_form,
        }
        return render(request, 'jornal/login.html', contexto)

    def post(self,request):
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = authenticate(request, email=user_form.email, password=user_form.password)
            if user is not None:
                login(request, user)
                return redirect('jornal:index')
            else:
                messages.error(request, 'Email ou senha invalidos')
                return redirect('jornal:login')
        else:
            contexto ={
                'user_form':user_form,
            }
            return render(request, 'jornal/login.html', contexto)

class register_view(TemplateView):
    def get(self,request):
        user_form = UserForm
        usuario_form = UsuarioForm
        contexto = {
            'user_form':user_form,
            'usuario_form':usuario_form
        }
        return render(request,'jornal/register.html',contexto)
    def post(self, request):
        user_form = UserForm(request.POST)
        usuario_form = UsuarioForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            return redirect('jornal:login')
        else:
            contexto = {
                'user_form':user_form,
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
        return render(request, "jornal/noticia/detalhe.html", {"noticia":noticia})

