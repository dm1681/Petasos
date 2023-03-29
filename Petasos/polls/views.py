from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Question

# Create your views here.

def index(request):
    """
    Index page response.
    """
    latest_quesiton_list = Question.objects.order_by("-pub_date")[:5]
    context={
        'latest_question_list' : latest_quesiton_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    """
    Returns a view of the details for the selected question
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})


def results(request, question_id):
    """
    Returns a view of the resultss for the selected question
    """
    return HttpResponse(f"You are looking at the results for question {question_id}")

def vote(request, question_id):
    """
    Returns a view of the votes for the selected question
    """
    return HttpResponse(f"You are voting on question {question_id}")
