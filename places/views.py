from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Place


def index(request):
    template = loader.get_template("index.html")

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
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
