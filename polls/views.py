# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.http import HttpResponse , Http404
import datetime

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def time(request):
    now = datetime.datetime.now()
    html = "<html><body>it is now %s.</body></html>" % now
    return HttpResponse(html)

def index(request):
    return HttpResponse("hello world")

def search(request):
    return render_to_response('search.html')

def searchform(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
