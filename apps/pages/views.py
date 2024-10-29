from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from apps.package.forms import SubscriptionForm

from apps.pages.models import TourCategory


def destination(request):
    return render(request, 'destination.html')


def explore_tour(request: WSGIRequest):
    subs = SubscriptionForm(request.POST or None, initial={'persons': 'ONE', 'kids': 1})
    return render(request=request, template_name='tour.html', context={
        "tour_category": TourCategory.objects.all(),
        "subs": subs,
    })


def travel_booking(request):
    return render(request, 'booking.html')


def our_gallery(request):
    return render(request, 'gallery.html')


def travel_guide(request):
    return render(request, 'guides.html')


def testimonial(request):
    return render(request, 'testimonial.html')
