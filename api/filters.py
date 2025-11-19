import django_filters
from .models import Movie, Genre, Country, PostType


class MovieFilter(django_filters.FilterSet):
    type= django_filters.ModelChoiceFilter(field_name= 'post_type', queryset= PostType.objects.all(), label= 'movie_or_serial')

    director= django_filters.CharFilter(field_name= 'director', lookup_expr= 'icontains', label= 'director')

    movie_star= django_filters.CharFilter(field_name= 'movie_star', lookup_expr= 'icontains', label= 'movie star')

    min_year= django_filters.NumberFilter(field_name= 'creation_year', lookup_expr= 'gte', label= 'min year')
    max_year= django_filters.NumberFilter(field_name= 'creation_year', lookup_expr= 'lte', label= 'max year')

    min_rating= django_filters.NumberFilter(field_name= 'imdb', lookup_expr= 'gte', label= 'min rating')
    max_rating= django_filters.NumberFilter(field_name= 'imdb', lookup_expr= 'lte', label= 'max rating')

    genre= django_filters.ModelChoiceFilter(field_name= 'genre', queryset= Genre.objects.all(), label= 'genre')

    country= django_filters.ModelChoiceFilter(field_name= 'country', queryset= Country.objects.all(), label= 'country')

    class Meta:
        model= Movie
        fields= ('type', 'director', 'movie_star', 'min_year', 'max_year', 'country', 'genre', 'min_rating', 'max_rating')