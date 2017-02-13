from django.conf.urls import url

from server.views import ServerView

urlpatterns = [
    url(r'^$', ServerView.as_view(), name='server'),
    url(r'^(?P<server_id>\d+)/$', ServerView.as_view(), name='server'),
]
