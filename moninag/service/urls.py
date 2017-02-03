from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views

app_name = 'service'

urlpatterns = [
    url(r'^$', csrf_exempt(views.ServiceView.as_view()), name='service'),
    url(r'^(?P<service_id>\d+)/$', csrf_exempt(views.ServiceView.as_view()), name='service'),
]
