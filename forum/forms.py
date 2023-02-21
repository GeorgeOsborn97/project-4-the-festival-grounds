from .models import Rooms, Conversations, Comments
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Fieldset


class RoomForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Rooms
        fields = [
            'title',
            'description',
            'status',
            'tags',
            'cover_image',
        ]


class EditRoomForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditRoomForm, self).__init__(*args, **kwargs)
        self.fields['members'].required = False

    class Meta:
        model = Rooms
        fields = [
            'title',
            'description',
            'status',
            'tags',
            'cover_image',
            'members'
        ]


class ConversationForm(forms.ModelForm):
    class Meta:
        model = Conversations
        fields = [
            'title',
            'content',
        ]


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-exampleForm'

    class Meta:
        model = Comments
        fields = [
            'body',
            'conversation'
        ]


class EditCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = [
            'body',
        ]

