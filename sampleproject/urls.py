from django.conf.urls import *
from django.conf import settings
from django.views.generic import RedirectView


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # FOR DEBUG AND TEST ONLY
    (r'^.*switch/(?P<username>.*)/(?P<password>.*)/$', 'djflow.workflow.views.debug_switch_user'),
    # home page
    (r'^$', 'sampleproject.sampleapp.views.home'),
    # home redirection
    (r'^.*home/$', RedirectView.as_view(url='/')),
    # login/logout
    (r'^logout/$', 'django.contrib.auth.views.logout'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name':'djflow/login.html'}),
    # Example:
    (r'^sampleapp/', include('sampleproject.sampleapp.urls')),

    # Uncomment the next line to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # FOR TEST - insert before admin/(.*)
    (r'^admin/workflow/', include('djflow.apptools.urls_admin')),
    # special
    (r'^admin/apptools/', include('djflow.apptools.urls_admin')),

    # Uncomment the next line for to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    # workflow pages
    (r'^workflow/', include('djflow.urls')),
    # static files
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
