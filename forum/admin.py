from django.contrib import admin
from .models import Rooms, Tags
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Rooms)
class RoomsAdmin(SummernoteModelAdmin):

    summernote_fields = ('description')
