from django.urls import path

from musics.artists.views import artist, artists

app_name = 'artists'
urlpatterns = [
    path('<artist_id>', artist, name='artist'),
    path('', artists, name='artists'),
]