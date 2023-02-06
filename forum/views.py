from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Rooms, Conversations, Comments
from .forms import RoomForm, ConversationForm

# Create your views here.


#class RoomList(generic.ListView):
#    model = Rooms
#    queryset = Rooms.objects.order_by('created_on')
#    template_name = 'index.html'
#    paginate_by = 5


class RoomList(View):

    def get(self, request, *args, **kwargs):
        room_list = Rooms.objects.order_by('created_on')
        paginator = Paginator(room_list, 5)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'rooms_list': room_list,
            'page_obj': page_obj,
            'form': RoomForm()
        }
        return render(request, '../templates/index.html', context)

    def post(self, request, *args, **kwargs):
        room_list = Rooms.objects.order_by('created_on')
        paginator = Paginator(room_list, 5)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.instance.creator = request.user
            form.instance.slug = form.instance.title.replace(' ', '-')
            room = form.save(commit=False)
            
            room.save()
            form.instance.members.add(request.user)
        else:
            form = RoomForm()

        context = {
            'rooms_list': room_list,
            'page_obj': page_obj,
            'form': RoomForm(),
        }
        return render(request, '../templates/index.html', context)
    

#class YourRoomList(generic.ListView):
#    model = Rooms
#    queryset = Rooms.objects.order_by('created_on')
#    template_name = 'your_rooms.html'
#    paginate_by = 5


class YourRoomList(View):

    def get(self, request, *args, **kwargs):
        room_list = Rooms.objects.order_by('created_on')
        paginator = Paginator(room_list, 5)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'room_list': room_list,
            'page_obj': page_obj,
            'form': RoomForm()
        }
        return render(request, '../templates/your_rooms.html', context)

    def post(self, request, *args, **kwargs):
        room_list = Rooms.objects.order_by('created_on')
        paginator = Paginator(room_list, 5)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.instance.creator = request.user
            form.instance.slug = form.instance.title.replace(' ', '-')
            room = form.save(commit=False)
            
            room.save()
            form.instance.members.add(request.user)
        else:
            form = RoomForm()

        context = {
            'room_list': room_list,
            'page_obj': page_obj,
            'form': RoomForm(),
        }
        return render(request, '../templates/your_rooms.html', context)


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
            form.instance.members.add(request.user)
        else:
            form = RoomForm()

        context = {
            'form': RoomForm(),
        }
        return render(request, '../templates/add_room.html', context)


class RoomView(View):
    def get(self, request, slug, *args, **kwargs):
        room_queryset = Rooms.objects.all()
        room = get_object_or_404(room_queryset, slug=slug)
        conversation = room.conversations.order_by('created_on')

        room_form = RoomForm(request.POST, instance=room)

        if room_form.is_valid():
            room_form.save()

        form = ConversationForm(request.POST)

        if form.is_valid():
            form.instance.creator = request.user
            form.instance.slug = form.instance.title.replace(' ', '-')
            new_convo = form.save(commit=False)
            new_convo.room = room
            new_convo.save()
        else:
            form = ConversationForm()

        convo_queryset = Conversations.objects.filter(room=room)

        if convo_queryset.exists():
            #  convo = get_object_or_404(convo_queryset)
          #  comments = convo.conversation_comments.order_by('created_on')
            comment_queryset = Comments.objects.all()
            return render(
                request,
                'room_view.html',
                {
                 'room': room,
                 'conversation_list': conversation,
                 'comments': comment_queryset,
                 'room_form': room_form,
                 'conversation_form': form
                },
                )
        else:
            return render(
                request,
                'room_view.html',
                {
                 'conversation_list': conversation,
                 'room_form': room_form,
                 'conversation_form': form
                },
                )

    def post(self, request, slug, *args, **kwargs):
        room_queryset = Rooms.objects.all()
        room = get_object_or_404(room_queryset, slug=slug)
        conversation = room.conversations.order_by('created_on')

        room_form = RoomForm(request.POST, instance=room)

        if room_form.is_valid():
            room_form.save()

        form = ConversationForm(request.POST)

        if form.is_valid():
            form.instance.creator = request.user
            form.instance.slug = form.instance.title.replace(' ', '-')
            new_convo = form.save(commit=False)
            new_convo.room = room
            new_convo.save()
        else:
            form = ConversationForm()

        convo_queryset = Conversations.objects.filter(room=room)

        if convo_queryset.exists():
          #  convo = get_object_or_404(convo_queryset)
          #  comments = convo.conversation_comments.order_by('created_on')
            comment_queryset = Comments.objects.all()

            return render(
                request,
                'room_view.html',
                {
                 'room': room,
                 'conversation_list': conversation,
                 'comments': comment_queryset,
                 'conversation_form': form,
                 'room_form': room_form
                },
                )
        else:
            return render(
                request,
                'room_view.html',
                {
                 'conversation_list': conversation,
                 'conversation_form': form,
                 'room_form': room_form
                },
                )
        