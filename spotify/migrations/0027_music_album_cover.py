# Generated by Django 3.2.3 on 2021-06-07 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0026_auto_20210525_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='album_cover',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='spotify.album'),
        ),
    ]