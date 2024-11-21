from django.urls import path
from .views import login_view
from .views import login_view, logout_view  # Adicione logout_view aqui
from django.urls import path
from .views import login_view, logout_view, home, cadastro_view, pesquisa_view
from .views import listar_clientes

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home, name='home'),
    path('cadastro/', cadastro_view, name='cadastro'),
    path('pesquisa/', pesquisa_view, name='pesquisa'),
    path('clientes/lista/', listar_clientes, name='lista_clientes'),
]