# Generated by Django 3.2.3 on 2021-06-26 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0033_alter_playlist_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='image',
            field=models.CharField(blank=True, default='https://i.pinimg.com/originals/db/f0/98/dbf098866a153bc938dce016f180e397.jpg', max_length=256),
        ),
    ]