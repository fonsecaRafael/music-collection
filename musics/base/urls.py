from django.urls import path

from musics.base.views import home, sign_up, users, upgrade, downgrade


app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
    path('signup/', sign_up, name='signup'),
    path('users/', users, name='users'),
    path('users/upgrade/<user_id>', upgrade, name='upgrade'),
    path('users/downgrade/<user_id>', downgrade, name='downgrade'),
]