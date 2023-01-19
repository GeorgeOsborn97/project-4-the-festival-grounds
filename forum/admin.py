from django.contrib import admin
from .models import Rooms, Tags
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Rooms)
class RoomsAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description')


@admin.register(Tags)
class TagsAdmin(SummernoteModelAdmin):

    summernote_fields = ('tag')
