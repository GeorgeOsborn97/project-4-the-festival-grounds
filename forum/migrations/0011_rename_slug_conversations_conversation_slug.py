# Generated by Django 3.2.16 on 2023-01-26 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_auto_20230120_1134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversations',
            old_name='slug',
            new_name='conversation_slug',
        ),
    ]
