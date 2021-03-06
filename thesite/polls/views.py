from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import Question, Choice
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
                pub_date__lte=timezone.now()
                ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        print(request.POST)
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question':question,
            'error_message':"you didn't select a choice"},
                )
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse(
            "polls:results", args=(question.id,))
            )

def getChoice(request, question_id):
    choice_given_pk = Choice.objects.filter(question_id=question_id)
    output = ", ".join([c.choice_text for c in choice_given_pk]) 
    context = {
            'choice_given_pk': choice_given_pk
            }
    return render(request, 'polls/choice.html', context)
