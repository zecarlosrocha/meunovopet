from django.shortcuts import render

def index(request):
    context = {
        'curso': 'Programação web com Django Framework'
    }
    return render(request, 'index.html', context)

def doador(request):
    return render(request, 'doador.html')