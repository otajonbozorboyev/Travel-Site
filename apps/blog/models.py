from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='blog/images/')
    author = models.CharField(max_length=50)
    description = models.TextField()
    day = models.DateTimeField(auto_now_add=True)
    like = models.FloatField()
    comments = models.IntegerField()

    def __str__(self) -> str:
        return self.title

