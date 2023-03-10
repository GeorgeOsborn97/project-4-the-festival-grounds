from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Public'), (1, 'Private'))


# Tag model
class Tags(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.tag


# Room model
class Rooms(models.Model):
    title = models.CharField(max_length=200, unique=True)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='built_rooms'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    cover_image = CloudinaryField('image', default='placeholder')
    description = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    tags = models.ManyToManyField(Tags, related_name='room_tags')
    members = models.ManyToManyField(User, related_name='room_members')

    class Meta:
        verbose_name_plural = 'Rooms'

    def __str__(self):
        return self.title

    def number_of_members(self):
        return self.members.count()


# Conversation model
class Conversations(models.Model):
    room = models.ForeignKey(
        Rooms, on_delete=models.CASCADE, related_name='conversations'
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='conversations_starter'
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Converstaions'

    def __str__(self):
        return self.title


# Comment model
class Comments(models.Model):
    name = models.CharField(max_length=80)
    room = models.ForeignKey(
        Rooms, on_delete=models.CASCADE, related_name='room_comments'
    )
    conversation = models.ForeignKey(
        Conversations, on_delete=models.CASCADE, related_name='conversation_comments'
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.name
