from django.shortcuts import render


def index(request):
    jogos = {
        1: 'Jogo 01',
        2: 'Jogo 02',
        3: 'Jogo 03',
    }

    dados = {
        'nome_jogos': jogos
    }
    return render(request, 'index.html', dados)


def futebol(request):
    return render(request, 'futebol.html')
