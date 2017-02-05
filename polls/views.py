###################################
###########Soudeh Mousavi##########
############Jan 31 2017 ###########

#from django.http import Http404  # for raising HTTP404
#from django.shortcuts import render
#from django.template import loader

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Question, Choice

#### Amend Views

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Question.objects.order_by('-pub_date')[:5]

    ##### Amending get_queryset
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        #returns a queryset containing Questions whose pub_date is
        # less than or equal to - that is, earlier than or equal to - timezone.now.
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    ### new get_queryset
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
         selected_choice = question.choice_set.get(pk=request.POST['choice'])
     except (KeyError, Choice.DoesNotExist):
         # Redisplay the question voting form.
         return render(request, 'polls/detail.html', {
             'question': question,
             'error_message': "You didn't select a choice."
         })
     else:
         selected_choice.vote += 1
         selected_choice.save()
         # Always return an HttpResponseRedirect after successfully dealing
         # with POST data. This prevents data from being posted twice if a
         # user hits the Back button.
         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# Create your views here.

# #### the simplest viw possible to call the view, we need to map in a URL
# #### We need URLconf, to create URLconf in polls directory, create a file called urls.py
#
# def index(request):
#     ################################################################### 1st view
#     #return HttpResponse("Hello, World. You are at the poll index")
#
#     #################################################################### 2nd view
#     #latest_question_list = (Question.objects.order_by('-pub_date')[:5])
#     #output = ', '.join(
#     #    [q.question_text for q in latest_question_list])
#     #return HttpResponse(output)
#     ################################################################### 3rd view
#     #latest_question_list = (Question.objects.order_by('-pub_date')[:5])
#     #template = loader.get_template('polls/index.html')
#     #context = {
#     #   'latest_question_list':latest_question_list
#     #}
#     #return HttpResponse(template.render(context,request))
#     ################################################################### 4th view
#     latest_question_list = (Question.objects.order_by('-pub_date')[:5])
#     context = {
#        'latest_question_list':latest_question_list
#     }
#     return render(request, 'polls/index.html', context)
#
#
# def detail(request, question_id):
#     ##################################################################### this works for 1st - 4th view
#     #return HttpResponse("You are looking at question %s. " % question_id)
#
#     ##################################################################### Raising HTTP 404
#     #try:
#     #    question = Question.objects.get(pk=question_id)
#     #except Question.DoesNotExist:
#     #    raise Http404("Question does not exist")
#     #return render(request,'polls/detail.html',{'question':question})
#
#     ##################################################################### shortcut to use get() and raise HTTP 404
#     question = get_object_or_404(Question,pk =question_id)
#     return render(request, 'polls/detail.html',{'question':question})
#
#
# def results(request, question_id):
#     ##################################################################### this works for 1st - 4th and erorr
#     #response = "You are looking at the result of question %s. "
#     #return HttpResponse (response % question_id)
#
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request,'polls/results.html',{'question':question})
#
# def vote (request, question_id):
#     ##################################################################### this works for 1st - 4th and erorr
#     #return HttpResponse("You are voting on question %s ." % question_id)
#
#
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice."
#         })
#     else:
#         selected_choice.vote += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
