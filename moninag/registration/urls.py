from django.conf.urls import url
from registration.views import activate, login, auth, logout, register_user


urlpatterns = [
    # Auth
    url(r'^$', auth, name='auth'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^activate/(?P<activation_key>[a-z0-9]+)/$', activate, name='activate'),
    url(r'^register_user/$', register_user, name='register_user'),
]
