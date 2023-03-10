# Generated by Django 3.2.16 on 2023-02-22 11:35

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0013_alter_rooms_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='cover_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
