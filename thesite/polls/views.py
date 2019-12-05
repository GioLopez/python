from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Question, Choice
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    context = {
            "latest_question_list": latest_question_list,
            }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question}) 

def results(request, question_id):
    return HttpResponse("Your are watching results of question: {}".format(question_id))

def vote(request, question_id):
    return HttpResponse("You are voting question {}".format(question_id))

def getChoice(request, question_id):
    choice_given_pk = Choice.objects.filter(question_id=question_id)
    output = ", ".join([c.choice_text for c in choice_given_pk]) 
    context = {
            'choice_given_pk': choice_given_pk
            }
    return render(request, 'polls/choice.html', context)
