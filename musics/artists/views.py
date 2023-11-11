import requests
from django.shortcuts import render


def artist(request, artist_id):
    artist = {'id': artist_id}
    return render(request, 'artists/details.html', context={'artist': artist})


def artists(request):
    url = 'https://europe-west1-madesimplegroup-151616.cloudfunctions.net/artists-api-controller'
    headers = {'Authorization': 'Basic ZGV2ZWxvcGVyOlpHVjJaV3h2Y0dWeQ =='}
    response = requests.get(url, headers=headers)
    artists = response.json()

    return render(request, 'artists/artists.html', context={'response': artists})
