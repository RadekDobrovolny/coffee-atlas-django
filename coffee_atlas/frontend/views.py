from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Coffee


def index(request):
    coffees = Coffee.objects.all()
    template = loader.get_template('index.html')
    context = {
        'coffees': coffees,
    }
    return HttpResponse(template.render(context, request))

def map(request):
    coffees = Coffee.objects.all()
    template = loader.get_template('map.html')
    context = {
        'coffees': coffees,
    }
    return HttpResponse(template.render(context, request))