import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place


class Command(BaseCommand):
    help = "Upload JSON data to db."

    def add_arguments(self, parser):
        parser.add_argument(
            "json_urls",
            nargs="+",
            type=str,
            help="one or several url link(s) to json file(s) with location info"
        )

    def handle(self, *args, **options):
        for url in options["json_urls"]:
            response = requests.get(url)
            response.raise_for_status()
            payload = response.json()

            place, created = Place.objects.get_or_create(
                title=payload["title"],
                lon=payload["coordinates"]["lng"],
                lat=payload["coordinates"]["lat"],
                defaults={
                    "short_description": payload["description_short"],
                    "long_description": payload["description_long"],
                }
            )
            for number, img_url in enumerate(payload["imgs"]):
                response = requests.get(img_url)
                response.raise_for_status()

                file = ContentFile(response.content, name=f"{place} - {number}")

                place.images.create(
                    file=file,
                )

            self.stdout.write(
                self.style.SUCCESS(f"Successfully created place \"{place}\"")
            )
