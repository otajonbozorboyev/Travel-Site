from django.db import models


class Package(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='package/images/')
    hotel_name = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=50)
    day = models.SmallIntegerField()
    person = models.SmallIntegerField()
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.title


class BookingTour(models.Model):
    class PersonSelect(models.TextChoices):
        ONE = "Person 1",
        TWO = "Person 2",
        THREE = "Person 3"

    class KidsSelect(models.TextChoices):
        Kids_1 = "Kids 1",
        Kids_2 = "Kids 2",
        Kids_3 = "Kids 3"

    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    data_time = models.DateTimeField()
    destination = models.CharField(max_length=100)
    persons = models.CharField(choices=PersonSelect.choices, default=PersonSelect.ONE, max_length=50)
    kids = models.CharField(max_length=128, choices=KidsSelect.choices, default=KidsSelect.Kids_1)
    message = models.TextField()

    def __str__(self) -> str:
        return self.full_name



class Subscription(models.Model):
    email = models.EmailField()

    is_published = models.BooleanField(default=False)
    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email