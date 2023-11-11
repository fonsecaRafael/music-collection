from django.shortcuts import render

from musics.albums.models import Album


def albums(request):
    albums = Album.objects.all()
    return render(request, 'albums/albums.html', context={'albums': albums})
