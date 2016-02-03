from django.conf.urls import *
from django.conf import settings

from leave.forms import StartRequestForm, RequesterForm, CheckRequestForm

from os.path import join, dirname
_dir = join(dirname(__file__))

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # FOR DEBUG AND TEST ONLY
    (r'^.*/accounts/login.*switch/(?P<username>.*)/(?P<password>.*)/$', 'djflow.workflow.views.debug_switch_user', {'redirect':'/leave/'}),
    (r'^.*/switch/(?P<username>.*)/(?P<password>.*)/$', 'djflow.workflow.views.debug_switch_user'),
    # user connection
    (r'^.*/logout/$', 'django.contrib.auth.views.logout'),
    (r'^.*/accounts/login/$', 'django.contrib.auth.views.login', {'template_name':'djflow/login.html'}),
    
    # static
    (r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': join(_dir, 'media/img'), 'show_indexes': True}),
    (r'^files/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    
    # home redirection
    (r'^.*/home/$', 'django.views.generic.simple.redirect_to', {'url':'/leave/'}),
 
    # home page
    (r'^leave/$', 'django.views.generic.simple.direct_to_template', {'template':'leave.html'}),
    
    # starting application
    (r'^leave/start/$', 'djflow.apptools.views.start_application', {'process_name':'leave',
                                                                           'form_class':StartRequestForm,
                                                                           'template':'start_leave.html'}),
    
    # applications
    (r'^leave/checkstatus/(?P<id>.*)/$', 'djflow.apptools.views.edit_model', {'form_class':CheckRequestForm,
                                                                                     'template':'checkstatus.html'}),
    (r'^leave/checkstatus_auto/$', 'leavedemo.leave.views.checkstatus_auto', {'notif_user':True}),
    (r'^leave/refine/(?P<id>.*)/$', 'djflow.apptools.views.edit_model', {'form_class':RequesterForm,
                                                                                'template':'refine.html'}),
    (r'^leave/approvalform/(?P<id>.*)/$', 'djflow.apptools.views.edit_model', {'form_class':CheckRequestForm,
                                                                                      'template':'approval.html'}),
    (r'^leave/hrform/(?P<id>.*)/$', 'djflow.apptools.views.view_application', {'template':'hrform.html'}),
    (r'^leave/hr_auto/$', 'leavedemo.leave.auto.update_hr'),
    (r'^leave/finalinfo/(?P<id>.*)/$', 'djflow.apptools.views.view_application', {'template':'finalinfo.html'}),
    
     # administration
    (r'^leave/admin/apptools/', include('djflow.apptools.urls_admin')),
    (r'^leave/admin/workflow/', include('djflow.apptools.urls_admin')),
    (r'^leave/admin/graphics2/', include('djflow.graphics2.urls_admin')),
    (r'^leave/admin/(.*)', admin.site.root),
    
    # Goflow pages
    (r'^leave/', include('djflow.urls')),

    (r'^leave/send_mail/$', 'djflow.workflow.notification.send_mail'),
    
)
