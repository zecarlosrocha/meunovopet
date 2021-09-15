from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import Animal


def index(request):
    animais = Animal.objects.all()

    context = {
        'curso': 'Programação web com Django Framework',
        'animais': animais
    }
    return render(request, 'index.html', context)


def doador(request):
    return render(request, 'doador.html')


def animal(request, pk):
    #ani = Animal.objects.get(id=pk)
    ani = get_object_or_404(Animal, id=pk)

    context = {
        'animal': ani
    }
    return render(request, 'animal.html', context)


def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
