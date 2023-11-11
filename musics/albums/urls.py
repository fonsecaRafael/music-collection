from django.urls import path

from musics.albums.views import albums

app_name = 'albums'
urlpatterns = [
    path('', albums, name='albums'),
]