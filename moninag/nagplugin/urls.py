from django.conf.urls import url

from nagplugin.views import NagPluginView

urlpatterns = [
    url(r'^$', NagPluginView.as_view(), name='nagplugins'),
]
