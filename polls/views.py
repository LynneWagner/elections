from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from .models import Question, Choice, Poll, UserProfile
from .forms import UserForm, UserProfileForm
from django.views import generic


def index(request):
    context = {'questions': Question.objects.all()}
    return render(request, 'polls/index.html', context)

def poll(request):
    context = {'questions': Question.objects.all()}
    return render(request, 'polls/poll.html', context)

@login_required
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

@login_required
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

@login_required
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
    form = UserProfileForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(False)
            user.is_active = False
            user.save()

            UserProfile.objects.create(
                user=user,
                address=form.cleaned_data['address'],
                username=form.cleaned_data['username']
            )
            return HttpResponse('Thanks for Registering. Please expect your PIN in to be delivered in 7-10 business days.')
        #else:
         #   return render(request, 'polls/register.html', {'form': form})
           ## return HttpResponseRedirect(reverse, ('polls:registered'))
    else:
      ##  return render(request, 'polls/register.html', {'form': form})
     return render(request, 'polls/register.html', {'form': form})

def registered(request):
    context = {}
    return render(request, 'polls/registered.html', context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
