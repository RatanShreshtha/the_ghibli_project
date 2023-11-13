from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from content.models import Film, People, Specie


class SpecieFactory(DjangoModelFactory):
    class Meta:
        model = Specie

    id = Faker("uuid4")
    name = Faker("name")
    classification = Faker("word")


class FilmFactory(DjangoModelFactory):
    class Meta:
        model = Film
        django_get_or_create = ("id",)

    id = Faker("uuid4")
    title = Faker("sentence")
    original_title = Faker("sentence", nb_words=3)
    original_title_romanised = Faker("sentence", nb_words=3)
    image = Faker("image_url")
    banner = Faker("image_url")
    description = Faker("text")
    director = Faker("name")
    producer = Faker("name")
    release_date = Faker("date")
    running_time = Faker("pyint", min_value=0, max_value=600)
    rt_score = Faker("pyint", min_value=0, max_value=100)


class PeopleFactory(DjangoModelFactory):
    class Meta:
        model = People

    id = Faker("uuid4")
    name = Faker("name")
    age = Faker("pyint", min_value=0, max_value=100)
    gender = Faker("random_element", elements=("male", "female", "other"))
    eye_color = Faker("random_element", elements=("black", "brown", "white"))
    hair_color = Faker("random_element", elements=("black", "blue", "green", "brown", "white"))
    specie = SubFactory(SpecieFactory)
    films = SubFactory(FilmFactory)
