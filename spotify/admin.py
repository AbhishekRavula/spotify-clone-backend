from django.contrib import admin
from spotify.models import Music, Playlist, Artist, Album

# Register your models here.
admin.site.register(Music)
admin.site.register(Playlist)
admin.site.register(Artist)
admin.site.register(Album)
