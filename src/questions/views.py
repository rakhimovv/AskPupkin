from django.shortcuts import render
from django.views.generic import TemplateView
import json
from datetime import datetime
from django import http
from django.contrib import auth
from django.contrib.auth import models as auth_models
from django.views.decorators import csrf as csrf_decorators
from django.views.generic import base as base_views
from django.views.generic import detail as detail_views
from django.views.generic import edit as edit_views
from django.views.generic import list as list_views
import models


class Home(list_views.ListView):
    template_name = 'index.html'
    paginate_by = 10

    def get_queryset(self):
        if self.request.GET.get('by_rating'):
            queryset = models.Question.objects.get_popular()
        elif self.request.GET.get('by_tag'):
            queryset = models.Question.objects.get_by_tag(self.request.GET.get('by_tag'))
        else:
            queryset = models.Question.objects.get_last()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['by_rating'] = self.request.GET.get('by_rating', '')
        context['by_tag'] = self.request.GET.get('by_tag', '')
        return context


class Question(detail_views.SingleObjectMixin, list_views.ListView):
    template_name = 'question.html'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=models.Question.objects.all())
        return super(Question, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return self.object.responses.order_by('-creation_date').all()


class AskQuestion(TemplateView):
    template_name = 'addquestion.html'
