from .models import Rooms, Conversations, Comments
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Fieldset


class RoomForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
        self.fields['title'].initial = 'a title'

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
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-exampleForm'

    class Meta:
        model = Comments
        fields = [
            'name',
            'body',
            'conversation'
        ]


class EditCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = [
            'name',
            'body',
        ]

