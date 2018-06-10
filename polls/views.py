from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader

from .models import Choice, Question,Category


def index(request):
    category_list = Category.objects.values('category_text')
    template = loader.get_template('polls/index.html')
    context = {
        'category_list': category_list,
    }
    return HttpResponse(template.render(context, request))
def category_science(request):
	q="Science"
	question_list = Question.objects.filter(category_id=1)[:50]
	template = loader.get_template('polls/t1.html')
	context = {
        'question_list': question_list,
		'category':q,
    }
	return HttpResponse(template.render(context, request))
def category_general(request):
	pass
	q="General"
	question_list = Question.objects.filter(category_id=4)[:50]
	template = loader.get_template('polls/t1.html')
	context = {
        'question_list': question_list,
		'category':q,
    }
	return HttpResponse(template.render(context, request))
def category_lifestyle(request):
	pass
	q="Lifestyle"
	question_list = Question.objects.filter(category_id=2)[:50]
	template = loader.get_template('polls/t1.html')
	context = {
        'question_list': question_list,
		'category':q,
    }
	return HttpResponse(template.render(context, request))
def category_opinion(request):
	pass
	q="Opinion"
	question_list = Question.objects.filter(category_id=3)[:50]
	template = loader.get_template('polls/t1.html')
	context = {
        'question_list': question_list,
		'category':q,
    }
	return HttpResponse(template.render(context, request))
	
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Select a choice then click the vote button",
        })
    else:
        select_choice.votes += 1
        select_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
def question_list(request):
	question_list=Question.objects.order_by('id')
	template = loader.get_template('polls/list.html')
	context = {
		'question_list': question_list,
    }
	return HttpResponse(template.render(context, request))
def latest_questions(request):
	question_list=Question.objects.order_by('-pub_date')[:10]
	template = loader.get_template('polls/latest.html')
	context = {
		'question_list': question_list,
    }
	return HttpResponse(template.render(context, request))



def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


