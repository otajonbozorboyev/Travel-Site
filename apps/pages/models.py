from django.db import models


class TourCategory(models.Model):
    name = models.CharField(max_length=128)
    image = models.FileField(upload_to='tour_category/', max_length=200)
    status = models.BooleanField(default=False)
    sale = models.SmallIntegerField(default=0)
    city = models.SmallIntegerField(default=0)
    place = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

