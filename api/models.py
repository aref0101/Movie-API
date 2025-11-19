from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

# Create your models here.

class CustomUser(AbstractUser):
    name= models.CharField(max_length= 200)
    username= models.CharField(unique= True)
    bio= models.TextField(blank= True)

    USERNAME_FIELD= 'username'
    REQUIRED_FIELDS= []

    def __str__(self):
        return self.name


class Genre(models.Model):
    name= models.CharField(max_length= 200, unique= True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name= models.CharField(max_length= 200, unique= True)

    def __str__(self):
        return self.name
    

class PostType(models.Model):
    name= models.CharField(max_length= 200)
        
    def __str__(self):
        return self.name

class Movie(models.Model):
    picture= models.ImageField(upload_to= 'picture/')
    imdb= models.FloatField(validators= [MinValueValidator(1.0), MaxValueValidator(10.0)])
    post_type= models.ForeignKey(PostType, on_delete= models.CASCADE, related_name= 'post_type')
    title= models.CharField(max_length= 200)
    creation_year= models.PositiveIntegerField(validators= [MinValueValidator(1920), MaxValueValidator(2025)])
    time= models.CharField()
    genre= models.ManyToManyField(Genre, related_name= 'genres')
    director= models.CharField(max_length= 200)
    movie_star= models.CharField(max_length= 200)
    country= models.ManyToManyField(Country, related_name= 'countries')
    bio= models.TextField()
    bookmarked_by= models.ManyToManyField(settings.AUTH_USER_MODEL, related_name= 'bookmarked_movies', blank= True)
    created_at= models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.title