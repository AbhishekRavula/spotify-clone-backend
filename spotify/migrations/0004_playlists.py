# Generated by Django 3.2.3 on 2021-05-17 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0003_alter_music_music_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spotify.music')),
            ],
        ),
    ]
