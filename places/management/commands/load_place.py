import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place


class Command(BaseCommand):
    help = "Upload JSON data to db."

    def add_arguments(self, parser):
        parser.add_argument("json_urls", nargs="+", type=str)

    def handle(self, *args, **options):
        for url in options["json_urls"]:
            response = requests.get(url)
            response.raise_for_status()
            place_info = response.json()

            place, created = Place.objects.get_or_create(
                title=place_info["title"],
                description_short=place_info["description_short"],
                description_long=place_info["description_long"],
                lon=place_info["coordinates"]["lng"],
                lat=place_info["coordinates"]["lat"]
            )
            place.save()
            for number, img_url in enumerate(place_info["imgs"]):
                response = requests.get(img_url)
                response.raise_for_status()

                file = ContentFile(response.content, name=f"{place} - {number}")

                place.images.create(
                    file=file,
                )

            self.stdout.write(
                self.style.SUCCESS(f"Successfully created place \"{place}\"")
            )
