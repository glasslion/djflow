from django.conf.urls import *

urlpatterns = patterns('',
    (r'^processimage/(?P<process_id>.*)/pos_activity/$', 'djflow.graphics.views.pos_activity'),
)
