from django.conf.urls import url
from user_profile.views import profile


urlpatterns = [
    # User profile
    url(r'^(?P<id>[0-9]+)/$', profile, name='profile'),
]
