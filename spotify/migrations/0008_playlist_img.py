# Generated by Django 3.2.3 on 2021-05-17 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0007_auto_20210517_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='img',
            field=models.CharField(default=False, max_length=200),
            preserve_default=False,
        ),
    ]
