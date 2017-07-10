from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic import View
from .models import Question, Choice, Poll
from .forms import UserForm, UserProfileForm
from django.views import generic


def index(request):
    context = {'questions': Question.objects.all()}
    return render(request, 'polls/index.html', context)

def faqs(request):
    context = {}
    return render(request, 'polls/register.html', context)

def poll(request):
    context = {'questions': Question.objects.all()}
    return render(request, 'polls/poll.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except:
         return render(request, 'polls/detail.html', {
        'question': question,
        'error_message': "You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def verify(request):
    form = UserForm(request.POST or None)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('polls:poll'))
            else:
                return HttpResponse('Your Registration account is disabled.')
        else:
            print('Invalid login details: {0}, {1}'.format(username, password))
            return HttpResponse('Invalid login details supplied.<br/>Details given: <br/>' +
                                '<p style="text-indent: 25px;">Username: ' + username + '</p>' +
                                '<p style="text-indent: 25px;">Password: ' + password + '</p>')

    else:
        return render(request, 'polls/verify.html', {'form': form})

def register(request):
    form = UserProfileForm(request.POST or None)
    if request.method == 'POST':
        name = request.POST.get('name')
        registration_id = request.POST.get('registration_id')
        address = request.POST.get('address')

    return render(request, 'polls/register.html', {'form': form})


#def register(request):
#	registered = False

#	if request.method == 'POST':
#		user_form = UserForm(data=request.POST)
#		profile_form = UserProfileForm(data=request.POST)

#		if user_form.is_valid() and profile_form.is_valid():
#			user = user_form.save()

#			user.set_password(user.password)
#			user.save()

#			profile = profile_form.save(commit=False)
#			profile.user = user

#			profile.save()
#			registered = True
#		else:
#			print(user_form.errors, profile_form.errors)
#	else:
#		user_form = UserForm()
#		profile_form = UserProfileForm()

#	return render(request, 'polls/register.html',
#		{'user_form': user_form,
#		 'profile_form': profile_form,
#		 'registered': registered})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
