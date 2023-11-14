from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=50)
    description_short = models.CharField(verbose_name="short description", max_length=300)
    description_long = models.TextField(verbose_name="long description")
    lon = models.FloatField(verbose_name="longitude")
    lat = models.FloatField(verbose_name="latitude")

    def __str__(self):
        return self.title
