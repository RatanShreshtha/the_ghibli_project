from pytest_factoryboy import register

from .factories import FilmFactory, PeopleFactory, SpecieFactory

register(FilmFactory)
register(PeopleFactory)
register(SpecieFactory)
