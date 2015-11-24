import views
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic.edit import CreateView
from django.contrib.auth import decorators

from django.conf.urls.static import static

urlpatterns = patterns(
    '',
    url(r'^$', views.Home.as_view(), name='index'),
    # url(r'^questions/ask/$', views.AskQuestion.as_view(), name='ask'),
    # url(r'^questions/ask/$', CreateView.as_view(model = views.AskQuestion), name='ask'),
    url(r'^questions/ask/$', views.ask_question, name='ask'),
    url(r'^questions/(?P<pk>\d+)/$', views.QuestionView.as_view(), name='question'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
