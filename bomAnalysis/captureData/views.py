from django.shortcuts import render
from django.http import HttpResponse
from . models import data

# Create your views here.

def index(request):
    return HttpResponse("Have a good day!")

def history(request):
    allSamples=data.objects.all()
    return HttpResponse(allSamples)