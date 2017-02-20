from django.conf.urls import url
from registration.views import request_password_reset, confirm_password_reset, activate, login, auth, logout, register_user


urlpatterns = [
    url(r'^$', auth, name='auth'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^activate/(?P<activation_key>[a-z0-9]+)/$', activate, name='activate'),
    url(r'^register_user/$', register_user, name='register_user'),
    url(r'^reset_password', request_password_reset, name="reset_password"),
    url(r'^confirm_password_reset/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$', confirm_password_reset, name='confirm_password_reset')
]
