from django.conf.urls import url

from .views import CheckView


app_name = 'check'

urlpatterns = [
    url(r'^$', CheckView.as_view(), name='check'),
    url(r'^(?P<check_id>\d+)/$', CheckView.as_view(), name='check'),
]
