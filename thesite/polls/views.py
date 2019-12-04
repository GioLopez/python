from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Ey soul sister!, you are at home")

def detail(request, question_id):
    return HttpResponse("Your are in details of question: {}".format(question_id))

def results(request, question_id):
    return HttpResponse("Your are watching results of question: {}".format(question_id))

def vote(request, question_id):
    return HttpResponse("You are voting question {}".format(question_id))
