from django.conf.urls import *
import forms

urlpatterns = patterns('djflow.apptools.views',
    (r'^start/(?P<app_label>.*)/(?P<model_name>.*)/$', 'start_application'),
    (r'^start_proto/(?P<process_name>.*)/$', 'start_application', {'form_class':forms.DefaultAppStartForm, 'template':'djflow/start_proto.html'}),
    (r'^view_application/(?P<id>\d+)/$', 'view_application'),
    (r'^choice_application/(?P<id>\d+)/$', 'choice_application'),
    (r'^sendmail/$', 'sendmail'),
)
