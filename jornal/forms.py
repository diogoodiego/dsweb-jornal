import email
from django import forms
from django.forms import ModelForm, Textarea, TextInput, Select, ImageField, ChoiceField
from django.contrib.auth.models import User
from .models import Usuario

TIPO_CHOICES = (
    ('e','Editor'),
    ('l','Leitor')
)

class UsuarioForm(forms.Form):
    username = forms.CharField(max_length=150, widget= TextInput(attrs={'class': 'form-control','type': 'text','placeholder':'Digite o nome de usuário'}))
    email = forms.CharField(max_length=150, widget= TextInput(attrs={'class': 'form-control','type': 'email','placeholder':'Digite seu email'}))
    password = forms.CharField(max_length=150, widget= TextInput(attrs={'class': 'form-control','type': 'password','placeholder':'Digite sua senha'}))
    tipo = forms.ChoiceField(choices=TIPO_CHOICES)
    imagem = ImageField()

    username.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control','type': 'password'})
    tipo.widget.attrs.update({'class': 'form-select'})

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150, widget= TextInput(attrs={'class': 'form-control','type': 'password'}))

    username.widget.attrs.update({'class': 'form-control'})
    # password.widget.attrs.update({'class': 'form-control','type': 'password'})