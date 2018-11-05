from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import shlex
from subprocess import Popen
from subprocess import run

def index(request):
    template = loader.get_template('video-index.html')

    context = {
    }
    
    return HttpResponse(template.render(context, request))

def live(request):
    template = loader.get_template('video-live.html')

    btnpicamstate = request.GET.get("btnpicamstate", "")

    context = {
        "btnpicamstate" : btnpicamstate
    }
    
    if btnpicamstate == 'on':
        pscmd = shlex.split("sudo systemctl start picam.service")
        run(pscmd)
    if btnpicamstate == 'off':
        pscmd = shlex.split("sudo systemctl stop picam.service")
        run(pscmd)

    return HttpResponse(template.render(context, request))