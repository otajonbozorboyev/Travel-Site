from django.urls import path
from .views import packageView

urlpatterns = [
    path('', packageView, name='package'),
]
