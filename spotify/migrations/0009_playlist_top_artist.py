# Generated by Django 3.2.3 on 2021-05-17 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0008_playlist_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='top_artist',
            field=models.CharField(default=False, max_length=100),
            preserve_default=False,
        ),
    ]