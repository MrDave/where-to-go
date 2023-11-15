from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=50)
    description_short = models.CharField(verbose_name="short description", max_length=300)
    description_long = models.TextField(verbose_name="long description")
    lon = models.FloatField(verbose_name="longitude")
    lat = models.FloatField(verbose_name="latitude")

    def __str__(self):
        return self.title


class Image(models.Model):
    file = models.ImageField(verbose_name="image file")
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="images")
    priority = models.IntegerField()

    class Meta:
        ordering = ["place", "priority"]

    def __str__(self):
        return f"{self.priority}. {self.place}"
