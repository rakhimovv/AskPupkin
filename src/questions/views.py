from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.views.generic import detail as detail_views
from django.views.generic import list as list_views
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormMixin
from django import http
from django.conf.urls import url
from django.shortcuts import render, redirect
from questions.models import Question, Response
from tags_likes.models import Tag, QuestionLike, ResponseLike
from django.views.generic.edit import CreateView
from forms import AddQuestionForm, AddAnswerForm
from django.core.mail import send_mail
import models
from django.conf import settings


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


class QuestionView(detail_views.SingleObjectMixin, list_views.ListView, FormMixin):
    model = Response
    form_class = AddAnswerForm
    template_name = 'question.html'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.object = models.Question.objects.get_by_id(kwargs['pk'])
        return super(QuestionView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return self.object.responses.order_by('-creation_date').reverse()

    def get_context_data(self, **kwargs):
        context = super(QuestionView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        form = AddAnswerForm(request.POST or None)
        if not request.user.is_authenticated():
            return redirect('login')

        if form.is_valid():
            question = models.Question.objects.get_by_id(kwargs['pk'])
            new_response = Response(content=form.cleaned_data['content'],
                                    author=request.user,
                                    question=question)
            new_response.save()

            # Send email to question author
            if question.author.email:
                subject = 'New answer for \"' + question.title + '\"'
                message = str(request.build_absolute_uri()) + '#' + str(new_response.id)
                from_email = settings.EMAIL_HOST_USER
                to_email = str(question.author.email)
                send_mail(subject, message, from_email, [to_email], fail_silently=settings.DEBUG)

            return redirect('/questions/' + str(question.id) + '#' + str(new_response.id))

        return redirect(models.Question.objects.get_by_id(kwargs['pk']))


@login_required
def ask_question(request):
    form = AddQuestionForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_question = Question(title=form.cleaned_data['title'],
                                content=form.cleaned_data['content'],
                                author=request.user)
        new_question.save()

        tags_list = form.cleaned_data['tags'].split(" ")
        tags = []
        for tag_title in tags_list:
            t = Tag.objects.get_or_create(title=tag_title)
            tags.append(t)

        for (key, value) in tags:
            new_question.tags.add(key)

        new_question.save()

        return redirect(new_question)

    return render(request, 'addquestion.html', {
        'form': form,
    })
