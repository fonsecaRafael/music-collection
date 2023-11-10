from django.urls import path

from musics.artists.views import artist


app_name = 'artists'
urlpatterns = [
    path('<artist_id>', artist, name='artist'),
]