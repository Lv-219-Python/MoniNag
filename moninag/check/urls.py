from django.conf.urls import url

from check.views import CheckView

urlpatterns = [
    url(r'^$', CheckView.as_view(), name='check'),
    url(r'^(?P<check_id>\d+)/$', CheckView.as_view(), name='check'),
]
