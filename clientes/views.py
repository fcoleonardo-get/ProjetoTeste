#from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import render
from django.shortcuts import render, redirect  # Para renderizar templates e redirecionar URLs
from .forms import ClienteForm  # Importa o formulário criado para o cadastro
from django.contrib.auth.models import User
from .models import Cliente  # Certifique-se de importar o modelo



def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redireciona para 'home' se estiver logado

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    return render(request, 'clientes/login.html', {'form': form})



def home(request):
    return HttpResponse("Bem-vindo, você está logado!")


def logout_view(request):
    logout(request)
    return redirect('login')

# View para renderizar a página inicial
def home(request):
    return render(request, 'clientes/home.html')

# View para renderizar a página de cadastro
def cadastro_view(request):
    return render(request, 'clientes/cadastro.html')

# View para renderizar a página de pesquisa
def pesquisa_view(request):
    return render(request, 'clientes/pesquisa.html')

# View responável por processar o formulário de cadastro

def cadastro_view(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            
            # Verificar se o nome de usuário já existe
            if User.objects.filter(username=cliente.nome).exists():
                cliente.user = User.objects.create(username=f"{cliente.nome}_unique")
            else:
                cliente.user = User.objects.create(username=cliente.nome)
                
            cliente.save()
            return redirect('home')
    else:
        form = ClienteForm()
        
    return render(request, 'clientes/cadastro.html', {'form': form})


def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista.html', {'clientes': clientes})
