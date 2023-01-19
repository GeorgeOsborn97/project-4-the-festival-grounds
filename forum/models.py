from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, 'Public'), (1, 'Private'))


class Tags(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Tags'


class Rooms(models.Model):
    title = models.CharField(max_length=200, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='built_rooms')
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    cover_image = CloudinaryField('image', default='placeholder')
    description = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    tags = models.ManyToManyField(Tags, related_name='room_tags')
    members = models.ManyToManyField(User, related_name='room_members')

    class Meta:  
        verbose_name_plural = 'Rooms'

