from django.shortcuts import render
from .models import Jogo


def index(request):
    jogos = Jogo.objects.all()

    dados = {
        'jogos': jogos
    }
    return render(request, 'index.html', dados)


def futebol(request):
    return render(request, 'futebol.html')
