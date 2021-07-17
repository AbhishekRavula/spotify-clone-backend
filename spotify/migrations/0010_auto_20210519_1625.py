# Generated by Django 3.2.3 on 2021-05-19 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0009_playlist_top_artist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlistmusic',
            name='music_id',
        ),
        migrations.AddField(
            model_name='playlistmusic',
            name='music_id',
            field=models.ManyToManyField(to='spotify.Music'),
        ),
    ]