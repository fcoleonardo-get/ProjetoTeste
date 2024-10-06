from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Cliente

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuário")
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'sexo', 'idade', 'endereco']  # Adicione os campos necessários