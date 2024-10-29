from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    icon = models.ImageField(upload_to='services/icons/%Y/%m/%d')

    def __str__(self) -> str:
        return self.title


class FeedbackClient(models.Model):
    full_name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='services/feedback_client/%Y/%m/%d')
    country = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.full_name