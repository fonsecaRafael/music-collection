from django.shortcuts import render, redirect

from musics.albums.forms import AlbumForm
from musics.albums.models import Album


def create_album(request):
    if request.method == "POST":
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            try:
                album_form.save()
                return redirect(Album)
            except:
                pass
    else:
        album_form = AlbumForm()
    return render(request, 'albums/create_album.html', {'album_form': album_form})


# Recovery
def albums(request):
    albums = Album.objects.all()
    return render(request, 'albums/albums.html', context={'albums': albums})


def album(request, album_id):
    album = Album.objects.get(id=album_id)
    return render(request, 'albums/album.html', context={'album': album})


def update_album(request, id):
    album = Album.objects.get(id=id)
    album_form = AlbumForm(request.POST, instance=album)
    if album_form.is_valid():
        album_form.save()
        return redirect(Album)
    return render(request, 'albums/update_album.html', {'album': album})


def delete_album(request, id):
    album = Album.objects.get(id=id)
    album.delete()
    return redirect(Album)
