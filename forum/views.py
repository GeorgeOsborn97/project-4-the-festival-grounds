from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Rooms

# Create your views here.


class RoomList(generic.ListView):
    model = Rooms
    queryset = Rooms.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 5
