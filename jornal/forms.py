from django import forms
from django.forms import ModelForm, Textarea, TextInput, Select
from django.contrib.auth.models import User
from .models import Usuario

#class UserForm(forms.Form):
#    username = forms.CharField(max_length=200)
#    email = forms.CharField(max_length=200)
#    password = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control form-control-sm','type':'password'}))

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username','email','password')
        widgets = {
            'username': TextInput(attrs={'class': 'form-control form-control-sm'}),
            'email': TextInput(attrs={'class': 'form-control form-control-sm','type':'email'}),
            'password': TextInput(attrs={'class': 'form-control form-control-sm', 'type': 'password'}),
        }

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'tipo' : Select(attrs={'class':'form-select'}),
        }