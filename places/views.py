from django.shortcuts import render
from django.http import HttpResponse
from .models import Place
from django.shortcuts import get_object_or_404


def index(request):
    places = Place.objects.all()

    features = []

    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lon, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": "lolkek"
            }
        }
        features.append(feature)

    places_geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    context = {"places": places_geojson}
    return render(request, "index.html", context)


def place_details(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    return HttpResponse(str(place.title))
