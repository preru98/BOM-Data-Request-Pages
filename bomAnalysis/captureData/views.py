from django.shortcuts import render
from django.http import HttpResponse
from . models import data
from django.utils import timezone
from datetime import datetime,timedelta

# Create your views here.

def index(request):
    return HttpResponse("Have a good day!")

def history(request):
    allSamples=data.objects.all().order_by('-pub_time')
    return HttpResponse(allSamples)

#One day only
def analysis(request):
    sampling_date = datetime.now() - timedelta(days=1)
    return request_interval(sampling_date)
    
#past<duration>days
def recent_day(request,duration):
    sampling_date = datetime.now() - timedelta(days=duration)
    return request_interval(sampling_date)

#past<duration>hours
def recent_hour(request,duration):
    sampling_date = datetime.now() - timedelta(hours=duration)
    return request_interval(sampling_date)
    
#past<duration>weeks
def recent_week(request,duration):
    sampling_date = datetime.now() - timedelta(weeks=duration)
    return request_interval(sampling_date)

def request_interval(sampling_date):
    today=datetime.now()
    present_day_samples=data.objects.filter(pub_time__range=(sampling_date ,today)).order_by('-pub_time')
    return HttpResponse(present_day_samples)


