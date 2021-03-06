#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from djflow.workflow.models import Process


from models import Graph

def graph(request, id, template='djflow/graphics/graph.html'):
    processes = Process.objects.all()
    graph = Graph.objects.get(id=(int(id)))
    return render_to_response(template, {'processes':processes, 'graph':graph})

def graph_save(request, id):
    # save positions TODO
    return HttpResponseRedirect('..')
