from django.shortcuts import render
from . models import About, Guide
from apps.package.forms import SubscriptionForm


def aboutView(request):
    about = About.objects.all()
    guide = Guide.objects.all().order_by('-id')[:5]
    subs = SubscriptionForm(request.POST or None, initial={'persons': 'ONE', 'kids': 1})
    return render(request, 'about.html', {
        'abouts': about,
        'guides': guide,
        "subs": subs
    })