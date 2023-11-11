from django.shortcuts import render


def artist(request, artist_id):
    artist = {'id': artist_id}
    return render(request, 'artists/details.html', context={'artist': artist})


def artists(request):
    artists = [
        {'name': 'artista 1'},
        {'name': 'artista 2'},
        {'name': 'artista 3'},
    ]
    return render(request, 'artists/artists.html', context={'artists': artists})
