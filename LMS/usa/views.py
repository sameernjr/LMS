from django.shortcuts import render
from .models import fullsail, oregonstate, coloradostate, saintlouis

# Create your views here.

def index(request):
    return render(request, 'usa/index.html',)
def fullsail_view(request):
    fullsail_objects=fullsail.objects.all()
    return render(request, 'usa/FullSail/courses.html', {'fullsail': fullsail})
def coloradostate(request):
    coloradostate_objects=coloradostate.objects.all()
    return render(request, 'usa/ColoradoState/courses.html', {'coloradostate': coloradostate})
def oregonstate(request):
    oregonstate_objects=oregonstate.objects.all()
    return render(request, 'usa/OregonState/courses.html', {'oregonstate': oregonstate})
def saintlouis(request):
    saintlouis_objects=saintlouis.objects.all()
    return render(request, 'usa/SaintLouis/courses.html', {'saintlouis': saintlouis})
