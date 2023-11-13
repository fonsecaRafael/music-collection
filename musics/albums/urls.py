from django.urls import path

from musics.albums.views import albums, album, create, update, delete

app_name = 'albums'
urlpatterns = [
    path('', albums, name='albums'),
    path('<album_id>', album, name='album'),
    path('create/', create, name='create'),
    path('update/<id>', update, name='update'),
    path('delete/<id>', delete, name='delete'),
]
