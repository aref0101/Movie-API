from django.contrib import admin
from .models import CustomUser, Genre, Country, Movie, PostType

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    search_fields= ['title']

class GenreAdmin(admin.ModelAdmin):
    search_fields= ['name']

class CountryAdmin(admin.ModelAdmin):
    search_fields= ['name']

class CustomUserAdmin(admin.ModelAdmin):
    search_fields= ['username']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(PostType)