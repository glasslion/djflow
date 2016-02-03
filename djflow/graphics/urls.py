from django.conf.urls import *
import views

urlpatterns = patterns('',
    (r'^(?P<id>.*)/save/$', views.graph_save),
    (r'^(?P<id>.*)/$', views.graph, {'template':'djflow/graphics/graph.html'}),
)
