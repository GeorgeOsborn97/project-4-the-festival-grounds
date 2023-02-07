from .models import Rooms, Conversations, Comments
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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = [
            'name',
            'body',
            'conversation'
        ]

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['conversation'] = forms.ModelChoiceField(queryset=Conversations.objects.all())
