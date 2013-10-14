# coding=utf-8
import datetime
from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import Context
#from django.template.loader import get_template
#trzy ostatnię zastapione przez import funkcji render (ze zmiana w funkcji current)

def hello(request):
    return render(request, "hello.html")

def currentTime(request):
    now = datetime.datetime.now()
    return render(request, "current_datetime.html", {"current_date": now})

def hoursAhead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, "time_ahead.html", {"offset" : offset, "dt": dt})

'''
def hoursAhead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>Za %s h bedzie %s.</body></html>" %(offset, dt)
    return HttpResponse(html)
'''
    