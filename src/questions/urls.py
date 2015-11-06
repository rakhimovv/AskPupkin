import views
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.auth import decorators

from django.conf.urls.static import static

urlpatterns = patterns(
    '',
    url(r'^$', views.Home.as_view(), name='index'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}, name='logout'),
    url(r'^profiles/edit/$', views.ProfileEdit.as_view(), name='profile_edit'),
    url(r'^profiles/(?P<pk>\d+)/$', views.Profile.as_view(), name='profile'),
    url(r'^questions/ask/$', decorators.login_required(views.AskQuestion.as_view()), name='ask'),
    url(r'^questions/(?P<pk>\d+)/$', views.Question.as_view(), name='question'),
    url(r'^signup/$', views.Signup.as_view(), name='signup'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
