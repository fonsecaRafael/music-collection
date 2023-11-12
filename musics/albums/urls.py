from django.urls import path

from musics.albums.views import albums, album

app_name = 'albums'
urlpatterns = [
    path('', albums, name='albums'),
    path('<album_id>', album, name='album')
]