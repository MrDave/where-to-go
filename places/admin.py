from django.contrib import admin
from .models import *
from django.utils.html import format_html
from adminsortable2.admin import SortableTabularInline, SortableAdminBase


class ImageInline(SortableTabularInline):
    model = Image

    def image_thumbnail(self):
        return format_html(
            '<img src="{}" style="max-width:200px; max-height:200px"/>'.format(self.file.url)
        )

    readonly_fields = (image_thumbnail,)
    ordering = ["priority",]
    extra = 3


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["place", "file"]
    ordering = ["place"]
    raw_id_fields = ["place"]
