# Generated by Django 3.2.3 on 2021-06-17 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0031_music_is_liked'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='is_liked',
            new_name='liked_users',
        ),
    ]
