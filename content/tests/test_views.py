import factory
import pytest
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_api_key.models import APIKey


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def api_client_authenticated():
    _, key = APIKey.objects.create_key(name="test")
    authorization = f"Api-Key {key}"
    client = APIClient(headers={"Authorization": authorization})
    return client


@pytest.mark.django_db
class TestFilmViewSet:
    def test_no_api_key(self, api_client):
        response = api_client.get(reverse("film-list"))
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert response.data["detail"] == "Authentication credentials were not provided."

    def test_list_films(self, film_factory, api_client_authenticated):
        film_factory.create_batch(3)
        response = api_client_authenticated.get(reverse("film-list"))
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == 3

    def test_create_film(self, film_factory, api_client_authenticated):
        payload = factory.build(dict, FACTORY_CLASS=film_factory)
        response = api_client_authenticated.post(reverse("film-list"), payload)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_retrieve_film(self, film_factory, api_client_authenticated):
        film = film_factory()
        response = api_client_authenticated.get(reverse("film-detail", args=[film.id]))
        assert response.status_code == status.HTTP_200_OK
        assert response.data["title"] == film.title

    def test_update_film(self, film_factory, api_client_authenticated):
        film = film_factory()
        fake = Faker()
        payload = {
            "title": fake.name(),
            "description": fake.text(),
            "director": fake.name(),
            "producer": fake.name(),
            "release_date": fake.date(),
            "rt_score": fake.random_int(min=0, max=100),
        }
        response = api_client_authenticated.patch(reverse("film-detail", args=[film.id]), payload)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_delete_film(self, film_factory, api_client_authenticated):
        film = film_factory()
        response = api_client_authenticated.delete(reverse("film-detail", args=[film.id]))
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
