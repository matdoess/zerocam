# from django.shortcuts import render

# # Create your views here.

from django.http import HttpResponse
from django.template import loader

import shlex
from subprocess import Popen
from subprocess import run
from time import sleep

def index(request):
    template = loader.get_template('index.html')

    context = {
        'latest_question_list': 'Hi wie gehts',
    }
    return HttpResponse(template.render(context, request))

def form_submit(request):
    # template = loader.get_template('response.html')

    # context = {
    # }

    ssid="'" + request.POST.get("ssid", "") + "'"
    password="'" + request.POST.get("password", "") + "'"

    #print("SSID=","ssid"," Passwort=","password")
    pscmd = shlex.split("sudo /home/pi/zerocam/script/switchap.sh wifi " + ssid + " " + password)
    run(pscmd)

    # return HttpResponse(template.render(context, request))