from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question

# Create your views here.


def index(request):
    """ Eu quero criar na variável latest_question_list uma lista das últimas questões que foram criadas
    context = server para dizer o que vai aparece na página
    return: o que exatamente vai aparecer"""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

"""
def detail(request, question_id):
    return HttpResponse('Essa é a pergunta de número %s' % question_id)
"""

def results(request, question_id):
    question = Question(pk=question_id)
    return render(request, 'polls/results.html',  {'question': question})


def vote(request, question_id):
    # Pegando uma questão e testando se ela está numa lista. Testando se o objeto existe, caso não exista, dá erro 404
    question = get_object_or_404(Question, pk=question_id)
    try:
        # Se existir, ele vai seguir normalmente. Vai continuar tentando fazer as opções.
        # Ele não somente vai votar, e sim influenciar na base de dados
        # O que eu selecionar vai para a variável selected_choice
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    # Senão vai dar um erro na página 404
    except KeyError:
        return render(request, 'polls/vote.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:

        # Se der tudo certo, incrementa e salva as escolhas
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

