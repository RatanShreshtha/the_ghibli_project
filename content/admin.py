from django.contrib import admin

from content.models import Film, People, Specie

admin.site.site_header = "The Ghibli Project Admin"
admin.site.site_title = "The Ghibli Project Admin Portal"
admin.site.index_title = "Welcome to The Ghibli Project Portal"


class PeopleInline(admin.TabularInline):
    model = People
    extra = 0
    fields = ["name", "age", "gender", "eye_color", "hair_color", "specie"]


class FilmAdmin(admin.ModelAdmin):
    inlines = [PeopleInline]


class SpecieAdmin(admin.ModelAdmin):
    inlines = [PeopleInline]


admin.site.register(People)
admin.site.register(Film, FilmAdmin)
admin.site.register(Specie, SpecieAdmin)
