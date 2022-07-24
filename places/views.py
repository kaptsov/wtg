from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Place


def index(request):
    places = {
        'type': 'FeatureCollection',
        'features': []
    }
    for place in Place.objects.all().iterator():
        place_feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lng, place.lat]
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse('place_view', kwargs={'place_id':place.id})
            }
        }
        places['features'].append(place_feature)


    data = {'places': places}
    return render(request, 'index.html', context=data)


def place_view(request, place_id):

    place = get_object_or_404(Place, id=place_id)

    place_serialized = {
        "title": place.title,
        "imgs": [image.img_file.url for image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.lat,
            "lng": place.lng
        }
    }
    return JsonResponse(
        data=place_serialized,
        safe=False,
        json_dumps_params={'ensure_ascii': False, 'indent':2}
    )
