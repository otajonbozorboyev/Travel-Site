from django.shortcuts import render

def destinationView(request):
    return render(request, 'destination.html')

def explore_tourView(request):
    return render(request, 'tour.html')

def travel_bookingView(request):
    return render(request, 'booking.html')

def our_galleryView(request):
    return render(request, 'gallery.html')

def travel_guideView(request):
    return render(request, 'guides.html')

def testimonialView(request):
    return render(request, 'testimonial.html')