import pytest
from django.urls import reverse

from musics.django_assertions import assert_contains


@pytest.fixture
def response(client):
    response = client.get(reverse('base:home'))
    return response


def test_status_code(response):
    assert response.status_code == 200


def test_title(response):
    assert_contains(response, '<title>MC - Home</title>')


def test_home_link(response):
    assert_contains(response, f'href="{reverse('base:home')}">Music Collection</a>')


def test_favicon(response):
    assert_contains(response, f"img/favicon.png")

