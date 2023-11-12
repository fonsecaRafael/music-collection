from django.urls import path

from musics.albums.views import albums, album, create_album, update_album, delete_album

app_name = 'albums'
urlpatterns = [
    path('create_album', create_album, name='create_album'),
    path('', albums, name='albums'),
    path('<album_id>', album, name='album'),
    path('update/<id>', update_album, name='update_album'),
    path('delete/<id>', delete_album, name='delete_album'),
]

# from django.contrib import admin
# urlpatterns = [
# path('admin/', admin.site.urls),
# ]
