from django.db import models

# Create your models here.


class Event(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    event_date = models.DateTimeField()
    link = models.URLField(max_length=200, unique=True)

    def __str__(self):
        return self.title
