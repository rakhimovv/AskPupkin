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
    model = models.Question
    paginate_by = 10

    def get_queryset(self):
        queryset = super(Home, self).get_queryset()
        queryset = queryset.select_related()
        # if self.request.GET.get('by_rating'):
        #    queryset = queryset.order_by('-author__rating')
        if self.request.GET.get('by_tag'):
            queryset = queryset.order_by('-author__rating')
        else:
            queryset = queryset.order_by('-created')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['by_rating'] = self.request.GET.get('by_rating', '')
        return context


class Signup(TemplateView):
    template_name = 'signup.html'


class Question(TemplateView):
    template_name = 'question.html'


class ProfileEdit(TemplateView):
    template_name = 'settings.html'


class AskQuestion(TemplateView):
    template_name = 'addquestion.html'


class Profile(TemplateView):
    template_name = 'profile.html'
