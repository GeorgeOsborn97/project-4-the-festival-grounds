# Generated by Django 3.2.16 on 2023-01-20 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_auto_20230120_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rooms',
            name='tags',
        ),
        migrations.AddField(
            model_name='rooms',
            name='tags',
            field=models.ManyToManyField(related_name='room_tags', to='forum.Tags'),
        ),
    ]
