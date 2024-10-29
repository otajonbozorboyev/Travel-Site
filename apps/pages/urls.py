from django.urls import path
from .views import (destinationView,
                    explore_tourView,
                    travel_bookingView,
                    our_galleryView,
                    travel_guideView,
                    testimonialView)


urlpatterns = [
    path('destination/', destinationView, name='destination'),
    path('explore_tour/', explore_tourView, name='tour'),
    path('travel_booking/', travel_bookingView, name='booking'),
    path('our_gallery/', our_galleryView, name='gallery'),
    path('travel_guides/', travel_guideView, name='guides'),
    path('testimonial/', testimonialView, name='testimonial'),
]