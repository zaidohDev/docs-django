from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from polls.models import Question


def index(request):
    try:
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
