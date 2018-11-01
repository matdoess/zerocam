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
    template = loader.get_template('response.html')

    context = {
        'ssid': request.POST['ssid'],
        'password': request.POST['password'],
    }

    pscmd = shlex.split("sudo /home/pi/zerocam/script/switchap.sh wifi 'FRITZ!Box 7590 SR' 25902909888682070047")
    run(pscmd)

    return HttpResponse(template.render(context, request))