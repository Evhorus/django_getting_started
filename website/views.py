from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def welcome(request):
    return HttpResponse("welcome to Meting Planner!")

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

def aboutMe(request):
    return HttpResponse("Hi, I'm learning django :D, thanks for visit my page :3")