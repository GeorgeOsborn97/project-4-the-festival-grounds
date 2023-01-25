from .models import Rooms
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
