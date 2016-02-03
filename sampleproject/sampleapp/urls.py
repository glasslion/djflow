from django.conf.urls import *
import forms
import views

urlpatterns = patterns('djflow.apptools.views',
    # starting application
    (r'^start/$', 'start_application', {'process_name':'Sample process',
                                        'form_class':forms.SampleModelForm,
                                        'template':'sample/start.html'}),
    # applications provided by djflow.apptools
    (r'^apptools/', include('djflow.apptools.urls')),
    # applications
    (  r'^sample_edit/(?P<id>\d+)/$', 'edit_model', {'template':  'edit.html'}),
)

urlpatterns += patterns('',
    (r'^sample_myview/$', views.myview),
)

urlpatterns += patterns('djflow.runtime.views',
    (r'^mywork/$', 'mywork', {'template':'sample/mywork.html'}),
    (r'^mywork/activate/(?P<id>.*)/$', 'activate'),
    (r'^mywork/complete/(?P<id>.*)/$', 'complete'),
)
