from django.conf.urls import url

from user_profile.views import UserProfileView

urlpatterns = [
    url(r'^$', UserProfileView.as_view(), name='user_profile'),
    url(r'^(?P<user_id>\d+)/$', UserProfileView.as_view(), name='user_profile'),
]
