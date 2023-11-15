import pytest
from model_mommy import mommy


@pytest.fixture()
def logged_user(db, django_user_model):
    user_model = mommy.make(django_user_model)
    return user_model


@pytest.fixture()
def logged_client(logged_user, client):
    client.force_login(logged_user)
    return client