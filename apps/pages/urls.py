from django.urls import path
from .views import (destination,
                    destination_tab,
                    explore_tour,
                    travel_booking,
                    our_gallery,
                    travel_guide,
                    testimonial, 
                    gallery_tab)
from apps.package.views import packageView2


urlpatterns = [
    path('destination/', destination, name='destination'),
    path('destination-tab/tab-<int:tab_id>/', destination_tab, name='destination_tab'),

    path('our_gallery/', our_gallery, name='gallery'),
    path('gallery-tab/tab-<int:tab_id>/', gallery_tab, name='gallery_tab'),

    path('explore_tour/', explore_tour, name='tour'),
    path('packageView2/', packageView2, name='package2'),
    path('travel_booking/', travel_booking, name='booking'),
    path('travel_guides/', travel_guide, name='guides'),
    path('testimonial/', testimonial, name='testimonial'),
]
