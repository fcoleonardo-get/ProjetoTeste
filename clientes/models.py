
# Create your models here.


from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    sexo = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    idade = models.IntegerField()
    endereco = models.CharField(max_length=255, default='Desconhecido')


    def __str__(self):
        return self.nome
