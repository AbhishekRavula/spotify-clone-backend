from django.contrib.auth.models import User
from django.db import models
from rest_framework.authtoken.models import Token
from django.core.files.storage import FileSystemStorage


class Artist(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=30)
    image = models.CharField(max_length=256, blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, default=1)
    released_date = models.DateField()

    def __str__(self):
        return self.name


class Music(models.Model):
    name = models.CharField(max_length=20)
    artist = models.ManyToManyField(Artist)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, default=1)
    music_path = models.CharField(max_length=500)
    liked_users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name


class Playlist(models.Model):
    name = models.CharField(max_length=30)
    image = models.CharField(max_length=256, blank=True,
                             default="https://i.pinimg.com/originals/db/f0/98/dbf098866a153bc938dce016f180e397.jpg")
    description = models.CharField(max_length=100, null=True)
    music = models.ManyToManyField(Music, blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, default=41)

    def __str__(self):
        return self.name
