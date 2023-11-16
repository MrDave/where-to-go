from django.contrib import admin
from .models import *
from django.utils.html import format_html


class ImageInline(admin.TabularInline):
    model = Image

    def image_thumbnail(self):
        return format_html(
            '<img src="{}" style="max-width:200px; max-height:200px"/>'.format(self.file.url)
        )

    readonly_fields = (image_thumbnail,)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
