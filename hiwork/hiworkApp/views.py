from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse
from django.template import loader

from .models import Question


def index(request):
    return HttpResponse("INDEX Page application page")


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'htmml/detail.html', {'question': question})


# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'htmml/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
# #         return HttpResponseRedirect(reverse('hiworkApp:results', args=(question.id,)))


def main(request):
    return render(request, 'html/main.html')


def clientJob(request):
    return render(request, 'html/clientJob.html')


def devJob(request):
    # template_name = 'html/index.html'
    # return HttpResponse("Developer job application page")
    return render(request, 'html/devJob.html')