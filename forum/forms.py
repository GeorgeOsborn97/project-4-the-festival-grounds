from .models import Rooms, Conversations, Comments
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Fieldset


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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = [
            'name',
            'body',
            'conversation'
        ]

   