from django.shortcuts import render
from . models import About, Guide

def aboutView(request):
    about = About.objects.all()
    guide = Guide.objects.all().order_by('-id')[:5]
    return render(request, 'about.html', {
        'abouts': about,
        'guides': guide,
    })