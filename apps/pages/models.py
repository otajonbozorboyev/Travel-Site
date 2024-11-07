from django.db import models
from apps.core.models import BaseModel


class TourCategory(models.Model):
    name = models.CharField(max_length=128)
    image = models.FileField(upload_to='tour_category/', max_length=200)
    status = models.BooleanField(default=False)
    sale = models.SmallIntegerField(default=0)
    city = models.SmallIntegerField(default=0)
    place = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class DestinationCategory(BaseModel):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class DestinationImage(models.Model):
    img = models.ImageField(upload_to='images/DestionationImage')

    def __str__(self):
        return self.img.name


class Destination(models.Model):
    title = models.CharField(max_length=128)
    images = models.ManyToManyField(DestinationImage, blank=True)
    ctg = models.ForeignKey(DestinationCategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
