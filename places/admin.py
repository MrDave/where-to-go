from adminsortable2.admin import SortableTabularInline, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html

from .models import *


class ImageInline(SortableTabularInline):
    model = Image
    ordering = ["priority",]
    extra = 3

    def show_image_thumbnail(self):
        return format_html(
            "<img src='{}' style='max-width:200px; max-height:200px'/>",
            self.file.url
        )

    readonly_fields = (show_image_thumbnail,)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["place", "file"]
    raw_id_fields = ["place"]
