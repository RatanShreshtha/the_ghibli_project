import uuid

from django.db import models


class Film(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    original_title = models.CharField(max_length=200)
    original_title_romanised = models.CharField(max_length=200)
    image = models.URLField(blank=True, null=True)
    banner = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    director = models.CharField(max_length=200)
    producer = models.CharField(max_length=200)
    release_date = models.DateField("released on")
    running_time = models.PositiveSmallIntegerField()
    rt_score = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.title} ({self.original_title})"

    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Films"


class Gender(models.TextChoices):
    M = "1", "Male"
    F = "2", "Female"
    O = "3", "Other"


class Specie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    classification = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} ({self.classification})"


class People(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    gender = models.CharField(max_length=2, choices=Gender.choices)
    eye_color = models.CharField(max_length=200)
    hair_color = models.CharField(max_length=200)
    films = models.ForeignKey(Film, on_delete=models.CASCADE, related_name="people", related_query_name="people")
    specie = models.ForeignKey(Specie, on_delete=models.CASCADE, related_name="specie", related_query_name="specie")

    def __str__(self):
        return f"{self.name} ({self.age})"
