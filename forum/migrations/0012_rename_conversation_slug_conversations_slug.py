# Generated by Django 3.2.16 on 2023-01-26 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0011_rename_slug_conversations_conversation_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversations',
            old_name='conversation_slug',
            new_name='slug',
        ),
    ]
