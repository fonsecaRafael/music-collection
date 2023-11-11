from django.shortcuts import render


def artist(request, artist_id):
    artist = {'id': artist_id}
    return render(request, 'artists/details.html', context={'artist': artist})


def artists(request):
    artists = {'1': 'artista 1', '2': 'artista 2', '3': 'artista 3',}
    return render(request, 'artists/artists.html', context={'artists': artists})
