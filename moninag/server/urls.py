from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views

app_name = 'server'

urlpatterns = [
    url(r'^$', csrf_exempt(views.ServerView.as_view()), name='server'),
    url(r'^(?P<server_id>\d+)/$', csrf_exempt(views.ServerView.as_view()), name='server'),
]
