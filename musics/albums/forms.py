from django import forms

from musics.albums.models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"
