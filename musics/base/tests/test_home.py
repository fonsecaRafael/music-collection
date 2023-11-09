from django.test import Client

from musics.django_assertions import assert_contains


def test_status_code(client: Client):
    response = client.get('/')
    assert response.status_code == 200


def test_title(client: Client):
    response = client.get('/')
    assert_contains(response, '<title>Music Collection</title>')
