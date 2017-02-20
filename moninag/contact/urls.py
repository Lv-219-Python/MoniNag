from django.conf.urls import url

from .views import ContactView


urlpatterns = [
    url(r'^$', ContactView.as_view(), name='contacts'),
    url(r'^(?P<contact_id>\d+)/$', ContactView.as_view(), name='contact'),
]
