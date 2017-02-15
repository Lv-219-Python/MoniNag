from django.conf.urls import url

from . import views

app_name = 'nagplugin'

urlpatterns = [
    url(r'^$', views.NagPluginView.as_view(), name='nagplugins'),
]
