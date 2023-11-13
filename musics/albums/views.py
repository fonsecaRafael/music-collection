from django.shortcuts import render, redirect

from musics.albums.forms import AlbumForm
from musics.albums.models import Album


def create(request):
    if request.method == "POST":
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            try:
                album_form.save()
                return redirect(Album())
            except:
                pass
    else:
        album_form = AlbumForm()
    return render(request, 'albums/create.html', {'album_form': album_form})


# Recovery
def albums(request):
    albums = Album.objects.all()
    return render(request, 'albums/albums.html', context={'albums': albums})


def album(request, album_id):
    album = Album.objects.get(id=album_id)
    return render(request, 'albums/album.html', context={'album': album})


def update(request, id):
    album = Album.objects.get(id=id)
    album_form = AlbumForm(request.POST, instance=album)
    if album_form.is_valid():
        album_form.save()
        return redirect(album)
    return render(request, 'albums/update.html', {'album': album})


def delete(request, id):
    album = Album.objects.get(id=id)
    album.delete()
    return redirect(album)
