from .models import Rooms, Conversations
from django import forms


class RoomForm(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = [
            'title',
            'description',
            'status',
            'tags',
            'cover_image',
        ]


class ConversationForm(forms.ModelForm):
    class Meta:
        model = Conversations
        fields = [
            'title',
            'content',
        ]
