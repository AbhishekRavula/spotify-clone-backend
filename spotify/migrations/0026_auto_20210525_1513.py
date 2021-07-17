# Generated by Django 3.2.3 on 2021-05-25 09:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0025_album_artist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CreatePlaylist',
        ),
        migrations.RemoveField(
            model_name='music',
            name='genre',
        ),
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='album',
            name='released_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]