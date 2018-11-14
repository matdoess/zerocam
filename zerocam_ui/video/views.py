from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import shlex
from subprocess import Popen
from subprocess import run
from subprocess import PIPE

from time import sleep

def index(request):
    template = loader.get_template('video-index.html')

    context = {
    }
    
    return HttpResponse(template.render(context, request))

def live(request):
    #sleep(5)
    template = loader.get_template('video-live.html')

    btnpicamstate = request.GET.get("btnpicamstate", "")

    btnpicamstatechange = False
    if btnpicamstate == 'on':
        btnpicamstatechange = True
        pscmd = shlex.split("sudo systemctl start picam.service")
        run(pscmd)
    if btnpicamstate == 'off':
        btnpicamstatechange = True
        pscmd = shlex.split("sudo systemctl stop picam.service")
        run(pscmd)
    if btnpicamstatechange:
        sleep(2)

    pscmd = shlex.split("systemctl is-active picam.service")
    picamstaterun = run(pscmd, stdout=PIPE)
    picamstaterunout = picamstaterun.stdout.decode('utf-8')
    if "inactive" in picamstaterunout:
        picamstate = False # "off"
    elif "active" in picamstaterunout:
        picamstate = True #"on"
    else:
        picamstate = None #"undefined"

    context = {
        "btnpicamstate" : btnpicamstate,
        "picamstate" : picamstate
    }

    return HttpResponse(template.render(context, request))