from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from .models import Place


def index(request):
    places = Place.objects.all()

    features = [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lon, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse("place-details", kwargs={"place_id": place.id})
            }
        }
        for place in places
    ]

    places_geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    context = {"places": places_geojson}
    return render(request, "index.html", context)


def show_place_details(request, place_id):
    place = get_object_or_404(Place.objects.all().prefetch_related("images"), id=place_id)
    response = {
        "title": place.title,
        "imgs": [request.build_absolute_uri(image.file.url) for image in place.images.all()],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lng": place.lon,
            "lat": place.lat
        }
    }
    return JsonResponse(response, json_dumps_params={"ensure_ascii": False, "indent": 4})
