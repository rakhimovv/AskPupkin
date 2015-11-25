import views
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic.edit import CreateView
from django.contrib.auth import decorators

from django.conf.urls.static import static

urlpatterns = patterns(
    '',
    url(r'^$', views.Home.as_view(), name='index'),
    url(r'^questions/ask/$', views.ask_question, name='ask'),
    url(r'^questions/(?P<pk>\d+)/$', views.QuestionView.as_view(), name='question'),
    url(r'^like_question/$', views.like_question, name='like_question'),
    url(r'^like_answer/$', views.like_answer, name='like_answer'),
    url(r'^check_correct_answer/$', views.check_correct_answer, name='check-correct-answer'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
