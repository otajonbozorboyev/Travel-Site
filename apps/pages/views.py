from django.db.models import Count
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from apps.package.forms import SubscriptionForm
from apps.pages.models import TourCategory, DestinationCategory, Destination


def destination(request: WSGIRequest):
    destination_ctg = DestinationCategory.objects.all()
    destination = Destination.objects.prefetch_related('images').select_related('ctg')
    return render(request, 'destination.html', context={
        'destination_ctg': destination_ctg,
        'destination': destination.annotate(destination_num=Count('images'))
    })

def destination_tab(request: WSGIRequest, tab_id: int):
    try:
        request.session['tab_id'] = tab_id
        destination_ = Destination.objects.filter(ctg_id=tab_id)
        destination_ctg = DestinationCategory.objects.all()
        return render(request=request, template_name='tab.html', context={
            'destination_ctg': destination_ctg,
            "destination": destination_.annotate(destination_num=Count('images'))
        })
    except:
        raise Exception("Xatolik mavjud!")

def explore_tour(request: WSGIRequest):
    return render(request=request, template_name='tour.html', context={
        "tour_category": TourCategory.objects.all()
    })


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
