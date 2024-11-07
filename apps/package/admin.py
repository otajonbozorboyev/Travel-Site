from django.contrib import admin
from .models import Package, BookingTour, Subscription

admin.site.register(Package)
admin.site.register(BookingTour)
admin.site.register(Subscription)