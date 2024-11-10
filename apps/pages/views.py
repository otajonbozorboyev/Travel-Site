from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Count
from django.shortcuts import render, redirect
from apps.package.forms import SubscriptionForm, PackageForm
from apps.pages.models import TourCategory, OurCategory, Destination, Gallery


def destination(request: WSGIRequest):
    destination_ctg = OurCategory.objects.filter(status=False)
    destination = Destination.objects.prefetch_related('images').select_related('ctg')
    # print(destination)
    subs = SubscriptionForm(request.POST or None, initial={'persons': 'ONE', 'kids': 1})
    print(destination)
    return render(request, 'destination.html', context={
        'destination_ctg': destination_ctg,
        'destination': destination.annotate(destination_num=Count('images')),
        'subs':subs,
    })

def destination_tab(request: WSGIRequest, tab_id: int):
    try:
        request.session['tab_id'] = tab_id
        destination_ = Destination.objects.filter(ctg_id=tab_id)
        destination_ctg = OurCategory.objects.filter(status=False)
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
    form = PackageForm(request.POST or None, initial={'persons': 'ONE', 'kids': 1})
    subs = SubscriptionForm(request.POST or None, initial={'persons': 'ONE', 'kids': 1})
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'booking.html', context={
        'form': form,
        "subs": subs
    })


def our_gallery(request):
    gallery_ctg = OurCategory.objects.filter(status=True)
    gallery = Gallery.objects.prefetch_related('images').select_related('ctg')
    subs = SubscriptionForm(request.POST or None, initial={'persons': 'ONE', 'kids': 1})
    return render(request, 'gallery.html', context={
        'gallery_ctg': gallery_ctg,
        'gallery': gallery,
        "subs": subs
    })

def gallery_tab(request: WSGIRequest, tab_id: int):
    try:
        request.session['gallery_tab_id'] = tab_id
        gallery = Gallery.objects.filter(ctg_id=tab_id)
        gallery_ctg = OurCategory.objects.filter(status=True)
        return render(request=request, template_name='gallery_tab.html', context={
            'gallery_ctg': gallery_ctg,
            "gallery": gallery
        })
    except:
        raise Exception("Xatolik mavjud!")



def travel_guide(request):
    return render(request, 'guides.html')


def testimonial(request):
    return render(request, 'testimonial.html')
