from django.conf.urls import url
from . import views
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^polls/', views.index, name='index'),
    url(r'^verify', views.verify, name='verify'),
    url(r'^poll', views.poll, name='poll'),
    url(r'^register', views.register, name='register'),
    url(r'^(?P<question_id>[0-9]+)/$',
        views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$',
        views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$',
        views.vote, name='vote'),
]