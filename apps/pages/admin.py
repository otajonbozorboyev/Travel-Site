from django.contrib import admin

from apps.pages.models import  TourCategory, Destination, OurCategory, Gallery, OurImage

# class TourCategoryAdmin(admin.ModelAdmin):
#     fields = ['__all__']

# def get_fields(self, request, obj=None):
#     fields = super().get_fields(request, obj)
#     if obj and obj.status:  # Agar status True bo'lsa
#         return fields  # Hammasi ko'rinadi
#     # Agar status False bo'lsa 'city' va 'place'ni olib tashlash
#     return [f for f in fields if f not in ('city', 'place')]


admin.site.register(TourCategory)
admin.site.register(Destination)
admin.site.register(OurCategory)
admin.site.register(OurImage)
admin.site.register(Gallery)
