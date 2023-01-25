from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Rooms
from .forms import RoomForm

# Create your views here.


#class RoomList(generic.ListView):
#    model = Rooms
#    queryset = Rooms.objects.order_by('created_on')
#    template_name = 'index.html'
#    paginate_by = 5


class RoomList(View):

    def get(self, request, *args, **kwargs):
        room = Rooms.objects.order_by('created_on')  
        paginator = Paginator(room, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(
            request,
            'index.html',
            {
             'page_obj': page_obj,
             'rooms_list': room,
            },
            )


# def add_room(request):
#    if request.method == 'POST':
#        form = RoomForm(request.POST, user)
#        if form.is_valid():
#            form.instance.creator = request.user.username
#            form.save()
#            return redirect('home')
#    form = RoomForm()
#    context = {
#        'form': form
#    }
#    return render(request, '../templates/add_room.html', context)


class addRoom(View):

    def get(self, request, *args, **kwargs):
        form = RoomForm(request.POST)
        context = {
            'form': RoomForm()
        }
        return render(request, '../templates/add_room.html', context)
    
    def post(self, request, *args, **kwargs):
        form = RoomForm(request.POST)
        if form.is_valid():
            form.instance.creator = request.user
            form.instance.slug = form.instance.title.replace(' ', '-')
            room = form.save(commit=False)
            room.save()
        else:
            form = RoomForm()

        context = {
            'form': RoomForm(),
        }
        return render(request, '../templates/add_room.html', context)

