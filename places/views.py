from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Place


def index(request):
    template = loader.get_template("index.html")

    places_geojson = {
      "type": "FeatureCollection",
      "features": [
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [37.62, 55.793676]
          },
          "properties": {
            "title": "«Легенды Москвы",
            "placeId": "moscow_legends",
            "detailsUrl": "./static/moscow_legends.json"
          }
        },
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [37.64, 55.753676]
          },
          "properties": {
            "title": "Крыши24.рф",
            "placeId": "roofs24",
            "detailsUrl": "./static/roofs24.json"
          }
        }
      ]
    }

    context = {"places": places_geojson}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
