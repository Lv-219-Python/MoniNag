"""moninag URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url, handler404
from utils.navigation_tree_view import get_navigation_tree

from moninag import views

urlpatterns = [
    url(r'^api/1/check/', include('check.urls')),
    url(r'^api/1/contact/', include('contact.urls')),
    url(r'^api/1/nagplugin/', include('nagplugin.urls')),
    url(r'^api/1/profile/', include('user_profile.urls')),
    url(r'^api/1/server/', include('server.urls')),
    url(r'^api/1/service/', include('service.urls')),
    url(r'^api/1/tree/', get_navigation_tree),
    url(r'^auth/', include('registration.urls')),
    url(r'^', include('home.urls')),
]

handler404 = views.error_404
