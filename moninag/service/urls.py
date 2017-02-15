from django.conf.urls import url

from service.views import ServiceView

urlpatterns = [
    url(r'^$', ServiceView.as_view(), name='service'),
    url(r'^(?P<service_id>\d+)/$', ServiceView.as_view(), name='service'),
]
