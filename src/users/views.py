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


class Signup(TemplateView):
    template_name = 'signup.html'


class ProfileEdit(TemplateView):
    template_name = 'settings.html'


class Profile(TemplateView):
    template_name = 'profile.html'
