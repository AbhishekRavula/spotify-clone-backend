# Generated by Django 3.2.3 on 2021-05-25 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0023_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='album',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='spotify.album'),
        ),
    ]
