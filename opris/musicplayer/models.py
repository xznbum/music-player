from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Compositor(models.Model):
    name = models.CharField(max_length=200)


class Genre(models.Model):
    name = models.CharField(max_length=200)


class MusicComposition(models.Model):
    compositor = models.ForeignKey(Compositor)
    name = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre)
    duration = models.FloatField()
    rating_listen = models.IntegerField(default=0)
    rating_user = models.IntegerField(default=0)


class Playlist(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    music_compositions = models.ManyToManyField(MusicComposition)


class Comment(models.Model):
    user = models.ForeignKey(User)
    music_composition = models.ForeignKey(MusicComposition)
    text = models.CharField(max_length=500)
    rating = models.IntegerField(default=0)