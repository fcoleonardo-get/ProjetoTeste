#from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import render

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

