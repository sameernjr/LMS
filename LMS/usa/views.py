from django.shortcuts import render
from .models import Video, fullsail, oregonstate, coloradostate, saintlouis

# Create your views here.

def index(request):
    video=Video.objects.all()
    return render(request, 'usa/index.html',)
def fullsail(request):
    fullsail=fullsail.objects.all()
    return render(request, 'usa/FullSail/courses.html', {'fullsail': fullsail})
def coloradostate(request):
    coloradostate=coloradostate.objects.all()
    return render(request, 'usa/ColoradoState/courses.html', {'coloradostate': coloradostate})
def oregonstate(request):
    oregonstate=oregonstate.objects.all()
    return render(request, 'usa/OregonState/courses.html', {'oregonstate': oregonstate})
def saintlouis(request):
    saintlouis=saintlouis.objects.all()
    return render(request, 'usa/SaintLouis/courses.html', {'saintlouis': saintlouis})
