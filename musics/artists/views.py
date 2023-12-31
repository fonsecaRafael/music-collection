import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


def send_get(url, headers):
    return requests.get(url, headers=headers).json()


@login_required()
@require_http_methods(["GET"])
def artist(request, artist_id):
    url = "https://europe-west1-madesimplegroup-151616.cloudfunctions.net/artists-api-controller?artist_id=" + artist_id
    artist = send_get(url, {'Authorization': 'Basic ZGV2ZWxvcGVyOlpHVjJaV3h2Y0dWeQ =='})

    return render(request, 'artists/details.html', context={'artist': artist})


@login_required()
@require_http_methods(["GET"])
def artists(request):
    artists = send_get(
        'https://europe-west1-madesimplegroup-151616.cloudfunctions.net/artists-api-controller',
        {'Authorization': 'Basic ZGV2ZWxvcGVyOlpHVjJaV3h2Y0dWeQ =='}
    )

    return render(request, 'artists/artists.html', context={'response': artists})
