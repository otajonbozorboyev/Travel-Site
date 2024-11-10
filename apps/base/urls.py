from django.urls import path
from .views import indexView
from apps.package.views import packageView2

urlpatterns = [
    path('', indexView, name='home'),
    path('packageView2/', packageView2, name='package2'),
]
