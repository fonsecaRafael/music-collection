from django.urls import path

from musics.base.views import home, sign_up


app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
    path('signup/', sign_up, name='signup'),
]