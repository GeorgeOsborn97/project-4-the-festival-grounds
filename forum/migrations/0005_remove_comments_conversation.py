# Generated by Django 3.2.16 on 2023-01-19 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20230119_1055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='conversation',
        ),
    ]
