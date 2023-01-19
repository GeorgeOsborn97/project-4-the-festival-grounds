# Generated by Django 3.2.16 on 2023-01-19 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0002_auto_20230119_0915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Converstations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversations_starter', to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversations', to='forum.rooms')),
            ],
            options={
                'verbose_name_plural': 'Converstaions',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('converstaion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversation_comments', to='forum.converstations')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_comments', to='forum.rooms')),
            ],
            options={
                'verbose_name_plural': 'Comments',
            },
        ),
    ]