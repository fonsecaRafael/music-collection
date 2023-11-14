from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', include('musics.base.urls')),
    path('artists/', include('musics.artists.urls')),
    path('albums/', include('musics.albums.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
