from django import forms
from .models import Usuario
from django.contrib.auth import authenticate, login

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields=['username', 'password', 'rol']