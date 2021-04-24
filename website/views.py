from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting

def welcome(request):
    return render(request, "website/welcome.html", {"meetings": Meeting.objects.all()})

def date(request):
    return HttpResponse("Cette page est servie à " + str(datetime.now()))

# Ajout d'une page

def moi(request):
    return HttpResponse("Salut moi c'est Alphonse et je suis là")