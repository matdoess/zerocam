from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('video-index.html')

    context = {
    }
    
    return HttpResponse(template.render(context, request))

def live(request):
    template = loader.get_template('video-live.html')

    context = {
    }
    
    return HttpResponse(template.render(context, request))