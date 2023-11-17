from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from musics.albums.forms import AlbumForm
from musics.albums.models import Album
from musics.artists.views import send_get


def get_artist_list():
    response = send_get(
        'https://europe-west1-madesimplegroup-151616.cloudfunctions.net/artists-api-controller',
        {'Authorization': 'Basic ZGV2ZWxvcGVyOlpHVjJaV3h2Y0dWeQ =='}
    )
    return [artist[0]['name'] for artist in response['json']]


@login_required()
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Album created successfully.')
                return redirect(Album())
            except:
                pass
        else:
            for key, error in form.errors.items():
                messages.error(request, f'{key.capitalize()}: {error[0]}')
            return render(request, 'albums/create.html', {'album_form': form, 'artists': get_artist_list()})

    else:
        form = AlbumForm()

    artists = get_artist_list()
    return render(request, 'albums/create.html', {'album_form': form, 'artists': artists})


@login_required()
@require_http_methods(["GET"])
def albums(request):
    albums = Album.objects.all()
    return render(request, 'albums/albums.html', context={'albums': albums})


@login_required()
@require_http_methods(["GET"])
def album(request, album_id):
    album = Album.objects.get(id=album_id)
    return render(request, 'albums/album.html', context={'album': album})


@login_required()
@require_http_methods(["GET", "POST"])
def update(request, id):
    album = Album.objects.get(id=id)
    if request.method == "POST":
        album_form = AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect(album)

    artists = get_artist_list()
    return render(request, 'albums/update.html', {'album': album, 'artists': artists})


@login_required()
@require_http_methods(["POST"])
def delete(request, id):
    album = Album.objects.get(id=id)
    album.delete()
    return redirect(album)
