from django.db import models
from django.urls import reverse


class Album(models.Model):
    artist = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    year = models.DateField()


    def get_absolute_url(self):
        return reverse('albums:')
