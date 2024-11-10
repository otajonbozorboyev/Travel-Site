from django.urls import path
from .views import packageView, packageView2

urlpatterns = [
    path('', packageView, name='package'),
    path('packageView2/', packageView2, name='package2'),
]
