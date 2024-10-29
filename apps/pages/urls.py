from django.urls import path
from .views import (destination,
                    explore_tour,
                    travel_booking,
                    our_gallery,
                    travel_guide,
                    testimonial)
from apps.package.views import packageView2

urlpatterns = [
    path('destination/', destination, name='destination'),
    path('explore_tour/', explore_tour, name='tour'),
    path('packageView2/', packageView2, name='package2'),
    path('travel_booking/', travel_booking, name='booking'),
    path('our_gallery/', our_gallery, name='gallery'),
    path('travel_guides/', travel_guide, name='guides'),
    path('testimonial/', testimonial, name='testimonial'),
]