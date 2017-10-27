# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from polls.models import Db
from django.db.models import Avg
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

def form(request):
    return render_to_response('h.html')

def searchform(request):
    if 'q' in request.GET:
        number = int(request.GET['q'])
        avrage = Db.objects.filter(film = number).aggregate(Avg('rate'))
        message = 'Film rate avrage: %r' % avrage
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)

def test(request):
    return render_to_response('test.html')
