from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Produto

# request -> 'url' 
# Uma view sempre é criado nos aplicativos
# Uma view django nada mais é do que uma função em python. 
# A função recebe uma variável chamada request e retorna a renderização desse request passando um template

def index(request):
    
    produtos = Produto.objects.all()
    
    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é legal!',
        'produtos': produtos
    }
    return render(request, 'index.html', context)

    
def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    # prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)
    
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)
    

def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404 )


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500 )
       