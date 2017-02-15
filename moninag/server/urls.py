from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ServerView.as_view(), name='servers'),
    url(r'^(?P<server_id>\d+)/$', views.ServerView.as_view(), name='server'),
]
