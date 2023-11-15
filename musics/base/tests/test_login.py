import pytest
from django.urls import reverse
from model_mommy import mommy

from musics.django_assertions import assert_contains


@pytest.fixture
def response(client):
    return client.get(reverse('login'))


def test_status_code(response):
    assert response.status_code == 200


@pytest.fixture()
def user(db, django_user_model):
    user_model = mommy.make(django_user_model)
    password = 'password'
    user_model.set_password(password)
    user_model.save()
    user_model.plain_password = password
    return user_model


@pytest.fixture()
def resp_post(client, user):
    return client.post(reverse('login'),
                       {'username': user.username,
                        'password': user.plain_password})


def test_login_redirect(resp_post):
    assert resp_post.status_code == 302
    assert resp_post.url == reverse('artists:artists')


@pytest.fixture
def resp_home(client):
    return client.get(reverse('base:home'))


def test_btn_login(resp_home):
    assert_contains(resp_home, 'Login')


def test_link_login(resp_home):
    assert_contains(resp_home, reverse('login'))
