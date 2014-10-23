from django.http.response import HttpResponse, Http404
from django.http import HttpRequest
#from django.template import Context
#from django.template.loader import get_template

from django.shortcuts import render_to_response
import datetime

def hello(request):
    return HttpResponse("Hello world, вы находитесь на странице {0}".format(request.path))

def current_datetime(request):
    now = datetime.datetime.now()
    #t = get_template('date/current_datetime.html')
    #html = t.render(Context({'current_date':now}))
    #return HttpResponse(html)

    return render_to_response('date/current_datetime.html', {'current_date':now})

def hours_ahead(request, offset):

    if offset == '1' or (len(offset)==2 and offset[1]=='1'):
        suffix = 'час'
    elif (int(offset) > 1 and int(offset) < 5) or (len(offset)==2 and (int(offset[1]) > 1 and int(offset[1]) < 5)):
        suffix = 'часа'
    else:
        suffix = 'часов'

    try:
        offset = int(offset)
    except: raise Http404()
    
    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    #html = "<html><body> Через {0} часов будет {1}.</body></html>".format(offset, dt)
    #return HttpResponse(html)

    return render_to_response('date/hours_ahead.html', {'hours_offset':offset, 'next_time':dt, 'suffix':suffix})

def display_meta(request):
    values = list(request.META.items())
    values.sort()
    values_of_requestAttr = []
    request_attr = [request.get_host, request.get_full_path, request.is_secure]
    string_request_attr = ['request.get_host', 'request.get_full_path', 'request.is_secure', 'request.path']

    for i in request_attr:
        values_of_requestAttr.append(i())

    values_of_requestAttr.append(request.path)
    list_httpRequest = list(zip(string_request_attr, values_of_requestAttr))

    return render_to_response('http_meta_info.html', {'meta_info':values, 'request_attr':list_httpRequest})