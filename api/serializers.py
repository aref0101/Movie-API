from rest_framework import serializers
from .models import Movie, Genre, Country, PostType
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
user= get_user_model()


class MovieSerializer(serializers.ModelSerializer):
    genre= serializers.SlugRelatedField(many= True, queryset= Genre.objects.all(), slug_field= 'name')
    country= serializers.SlugRelatedField(many= True, queryset= Country.objects.all(), slug_field= 'name')
    post_type= serializers.SlugRelatedField(queryset= PostType.objects.all(), slug_field= 'name')

    class Meta:
        model= Movie
        fields= ('id', 'picture', 'imdb', 'post_type', 'title', 'creation_year', 'time', 
                'genre', 'director', 'movie_star', 'country', 'bio', 'created_at')


class UserRegisterSerializer(serializers.ModelSerializer):
    password= serializers.CharField(write_only= True, min_length= 8,
    validators= [validate_password], style= {'input_type': 'password'})

    class Meta:
        model= user
        fields= ('name', 'username', 'bio', 'password')

    def create(self, validated_data):
        return user.objects.create_user(**validated_data)