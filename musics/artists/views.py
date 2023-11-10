from django.shortcuts import render


def artist(request, artist_id):
    artist = {'id': artist_id}
    return render(request, 'artists/details.html', context={'artist': artist})
