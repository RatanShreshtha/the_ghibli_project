from rest_framework import serializers

from .models import Film, People, Specie


class SpecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specie
        fields = ["id", "name", "classification"]


class PeopleSerializer(serializers.ModelSerializer):
    films = serializers.CharField(source="films.title")
    specie = SpecieSerializer()

    class Meta:
        model = People
        fields = ["id", "name", "age", "gender", "eye_color", "hair_color", "specie", "films"]


class FilmSerializer(serializers.ModelSerializer):
    people = PeopleSerializer(many=True, read_only=True)

    class Meta:
        model = Film
        fields = [
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
