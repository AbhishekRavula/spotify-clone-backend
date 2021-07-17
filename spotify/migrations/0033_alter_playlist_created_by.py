# Generated by Django 3.2.3 on 2021-06-26 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spotify', '0032_rename_is_liked_music_liked_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='created_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
