from django.conf.urls import url

from . import views

app_name = 'service'

urlpatterns = [
    url(r'^$', views.ServiceView.as_view(), name='service'),
    url(r'^(?P<service_id>\d+)/$', views.ServiceView.as_view(), name='service'),
]
