import pytest
from django.test import Client
from django.urls import reverse

from musics.django_assertions import assert_contains


@pytest.fixture
def response(client):
    response = client.get(reverse('home'))
    return response


def test_status_code(response):
    assert response.status_code == 200


def test_title(response):
    assert_contains(response, '<title>Music Collection</title>')


def test_home_link(response):
    assert_contains(response, f'href="{reverse('home')}">Music Collection</a>')
