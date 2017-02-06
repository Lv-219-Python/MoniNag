from django.conf.urls import url
from registration.views import activate, login, auth, logout, register_user

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # auth
    url(r'^$', auth, name='auth'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^activate/(?P<activation_key>[a-z0-9]+)/$', activate, name='activate'),
    url(r'^register_user/$', register_user, name='register_user')


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
