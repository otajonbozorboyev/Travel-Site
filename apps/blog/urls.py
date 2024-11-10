from django.urls import path
from .views import blogView
from apps.package.views import packageView2

urlpatterns = [
    path('', blogView, name='blog'),
    path('packageView2/', packageView2, name='package2'),
]
