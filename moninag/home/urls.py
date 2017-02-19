from django.conf.urls import url

from home.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
]
