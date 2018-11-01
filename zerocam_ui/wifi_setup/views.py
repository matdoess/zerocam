# from django.shortcuts import render

# # Create your views here.

from django.http import HttpResponse
from django.template import loader


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

    return HttpResponse(template.render(context, request))