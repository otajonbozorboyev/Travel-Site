from django.db import models


class ContactMe(models.Model):
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.phone


class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    is_published = models.BooleanField(default=False)

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name