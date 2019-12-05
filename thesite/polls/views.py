from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

from .models import Question, Choice
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    template = loader.get_template('polls/index.html')
    context = {
            "latest_question_list": latest_question_list,
            }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("Your are in details of question: {}".format(question_id))

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
