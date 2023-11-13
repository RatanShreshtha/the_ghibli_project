import pytest

from content.serializers import FilmSerializer, PeopleSerializer, SpecieSerializer


@pytest.mark.django_db
class TestFilmSerializer:
    def test_serializer_contains_expected_fields(self, film_factory):
        film = film_factory()
        serializer = FilmSerializer(instance=film)
        data = serializer.data
        assert set(data.keys()) == set(
            [
                "id",
                "title",
                "original_title",
                "original_title_romanised",
                "image",
                "banner",
                "description",
                "director",
                "producer",
                "release_date",
                "running_time",
                "rt_score",
                "people",
            ]
        )

    def test_serializer_data_matches_input_data(self, film_factory):
        film = film_factory()
        serializer = FilmSerializer(instance=film)
        data = serializer.data

        fields = [field.name for field in film._meta.fields]
        for field in fields:
            assert getattr(film, field) == data[field]


@pytest.mark.django_db
class TestSpecieSerializer:
    def test_serializer_contains_expected_fields(self, specie_factory):
        specie = specie_factory()
        serializer = SpecieSerializer(instance=specie)
        data = serializer.data
        assert set(data.keys()) == set(
            [
                "id",
                "name",
                "classification",
            ]
        )

    def test_serializer_data_matches_input_data(self, specie_factory):
        specie = specie_factory()
        serializer = SpecieSerializer(instance=specie)
        data = serializer.data

        fields = [field.name for field in specie._meta.fields]
        for field in fields:
            assert getattr(specie, field) == data[field]


@pytest.mark.django_db
class TestPeopleSerializer:
    def test_serializer_contains_expected_fields(self, people_factory):
        people = people_factory()
        serializer = PeopleSerializer(instance=people)
        data = serializer.data
        assert set(data.keys()) == set(["id", "name", "age", "gender", "eye_color", "hair_color", "specie", "films"])
