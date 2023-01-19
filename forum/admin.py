from django.contrib import admin
from .models import Rooms, Tags
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Rooms)
class RoomsAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'tags')
    list_display = ('title', 'slug', 'creator', 'created_on', 'status')
    search_fields = ['title', 'creator', 'tags']
    summernote_fields = ('description')


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    search_fields = ['tag']
