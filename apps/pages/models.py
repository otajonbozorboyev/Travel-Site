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


class OurCategory(BaseModel):
    name = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.name


class OurImage(models.Model):
    img = models.ImageField(upload_to='images/DestionationImage')
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.img.name


class Destination(models.Model):
    title = models.CharField(max_length=128)
    images = models.ManyToManyField(OurImage, blank=True)
    ctg = models.ForeignKey(OurCategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class Gallery(BaseModel):
    title = models.CharField(max_length=123)
    images = models.ManyToManyField(OurImage)
    ctg = models.ForeignKey(OurCategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title