"""
Definition of urls for rest_test.
"""

from datetime import datetime
from django.conf.urls import url, include
import django.contrib.auth.views


# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^api/blogs/'include('blogs.api.urls',namespace='api-blogs'))
]
