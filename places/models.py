from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    title = models.CharField(max_length=50, unique=True)
    short_description = models.TextField(verbose_name="short description", blank=True)
    long_description = tinymce_models.HTMLField(verbose_name="long description", blank=True)
    lon = models.FloatField(verbose_name="longitude")
    lat = models.FloatField(verbose_name="latitude")

    def __str__(self):
        return self.title


class Image(models.Model):
    file = models.ImageField(verbose_name="image file")
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="images")
    priority = models.PositiveIntegerField(default=0, db_index=True)

    def __str__(self):
        return str(self.file)

    class Meta:
        ordering = ["priority", "place"]
