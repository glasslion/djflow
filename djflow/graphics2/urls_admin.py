from django.conf.urls import *

urlpatterns = patterns('',
    (r'^processimage/(?P<process_id>.*)/pos_activity/$', 'djflow.graphics2.views.pos_activity'),
)
