from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.core.paginator import Paginator
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Rooms, Conversations, Comments
from .forms import RoomForm, EditRoomForm, ConversationForm, CommentForm, EditCommentForm, forms

# Create your views here.


class RoomList(View):

    def get(self, request, *args, **kwargs):
        room_list = Rooms.objects.order_by('created_on')
        paginator = Paginator(room_list, 5)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'rooms_list': room_list,
            'page_obj': page_obj,
            'form': RoomForm(request.POST, request.FILES)
        }
        return render(request, '../templates/index.html', context)

    def post(self, request, *args, **kwargs):
        room_list = Rooms.objects.order_by('created_on')
        paginator = Paginator(room_list, 5)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.creator = request.user
            form.instance.slug = form.instance.title.replace(' ', '-')
            room = form.save()
            
            room.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your room has successfully been created!'
            )
            form.instance.members.add(request.user)
        else:
            form = RoomForm()

        context = {
            'rooms_list': room_list,
            'page_obj': page_obj,
            'form': form,
        }
        return render(request, '../templates/index.html', context)
    

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
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.creator = request.user
            form.instance.slug = form.instance.title.replace(' ', '-')
            room = form.save(commit=False)
            
            room.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your room has successfully been created!'
            )
            form.instance.members.add(request.user)
            form.instance.members.add(request.user)
        else:
            form = RoomForm()

        context = {
            'room_list': room_list,
            'page_obj': page_obj,
            'form': RoomForm(),
        }
        return render(request, '../templates/your_rooms.html', context)


class RoomView(View):
    def get(self, request, slug, *args, **kwargs):
        room_queryset = Rooms.objects.all()
        room = get_object_or_404(room_queryset, slug=slug)
        conversation = room.conversations.order_by('created_on')
        if request.user not in room.members.all():
            room.members.add(request.user)
        
        room_form = EditRoomForm(instance=room)
        room_form.fields['members'] = forms.ModelMultipleChoiceField(
            room.members,
            widget=forms.CheckboxSelectMultiple
        )

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
            comment_queryset = Comments.objects.all().order_by('created_on')

            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment_form.instance.name = request.user
                new_comment = comment_form.save(commit=False)
                new_comment.room = room
                new_comment.save()
            else:
                comment_form = CommentForm()

            return render(
                request,
                'room_view.html',
                {
                 'room': room,
                 'conversation_list': conversation,
                 'comments': comment_queryset,
                 'room_form': room_form,
                 'conversation_form': form,
                 'comment_form': comment_form
                },
                )
        else:
            return render(
                request,
                'room_view.html',
                {
                 'room': room,
                 'conversation_list': conversation,
                 'room_form': room_form,
                 'conversation_form': form,
                },
                )

    def post(self, request, slug, *args, **kwargs):
        room_queryset = Rooms.objects.all()
        room = get_object_or_404(room_queryset, slug=slug)
        conversation = room.conversations.order_by('created_on')

        room_form = EditRoomForm(request.POST, request.FILES, instance=room)

        if room_form.is_valid():
            room_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'your room has successfully been edited!'
            )
        
        room_form.fields['members'] = forms.ModelMultipleChoiceField(
            room.members,
            widget=forms.CheckboxSelectMultiple
        )

        form = ConversationForm(request.POST)

        if form.is_valid():
            form.instance.creator = request.user
            form.instance.slug = form.instance.title.replace(' ', '-')
            new_convo = form.save(commit=False)
            new_convo.room = room
            new_convo.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'your conversation has successfully been started!'
            )
        else:
            form = ConversationForm()

        convo_queryset = Conversations.objects.filter(room=room)

        if convo_queryset.exists():
            comment_queryset = Comments.objects.all().order_by('created_on')

            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                comment_form.instance.name = request.user
                new_comment = comment_form.save(commit=False)
                new_comment.room = room
                new_comment.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'your comment has successfully been added!'
                )
            else:
                comment_form = CommentForm()

            return render(
                request,
                'room_view.html',
                {
                 'room': room,
                 'conversation_list': conversation,
                 'comments': comment_queryset,
                 'conversation_form': form,
                 'room_form': room_form,
                 'comment_form': comment_form
                },
                )
        else:
            return render(
                request,
                'room_view.html',
                {
                 'room': room,
                 'conversation_list': conversation,
                 'conversation_form': form,
                 'room_form': room_form,
                },
                )


class edit_conversation(View):
    def get(self, request, conversation_id, *args, **kwargs):
        conversation_queryset = Conversations.objects.all()
        convo = get_object_or_404(conversation_queryset, id=conversation_id)
        comment_queryset = Comments.objects.all()

        convo_form = ConversationForm(instance=convo)

        context = {
            'conversations': conversation_queryset,
            'conversation': convo,
            'comments': comment_queryset,
            'form': convo_form
         }
        return render(request, '../templates/edit_conversations.html', context)

    def post(self, request, conversation_id, *args, **kwargs):
        conversation_queryset = Conversations.objects.all()
        convo = get_object_or_404(conversation_queryset, id=conversation_id)
        slug = convo.room.slug
        comment_queryset = Comments.objects.all()

        convo_form = ConversationForm(request.POST, instance=convo)

        if convo_form.is_valid():
            convo_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'your conversation has successfully been edited!'
            )

        context = {
            'conversations': conversation_queryset,
            'conversation': convo,
            'comments': comment_queryset,
            'form': convo_form
         }
        return HttpResponseRedirect(reverse('in_room', args=[slug]))


class edit_comment(View):
    def get(self, request, comment_id, *args, **kwargs):
        comment_queryset = Comments.objects.all()
        comment = get_object_or_404(comment_queryset, id=comment_id)

        comment_form = EditCommentForm(instance=comment)

        context = {
            'comment': comment,
            'comments': comment_queryset,
            'form': comment_form
         }
        return render(request, '../templates/edit_comment.html', context)

    def post(self, request, comment_id, *args, **kwargs):
        comment_queryset = Comments.objects.all()
        comment = get_object_or_404(comment_queryset, id=comment_id)
        slug = comment.room.slug
        comment_form = EditCommentForm(request.POST, instance=comment)

        if comment_form.is_valid():
            comment_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'your comment has successfully been edited!'
            )

        context = {
            'comment': comment,
            'comments': comment_queryset,
            'form': comment_form
         }
        return HttpResponseRedirect(reverse('in_room', args=[slug]))


def delete_room(request, room_id):
    room = Rooms.objects.get(id=room_id)
    room.delete()
    messages.add_message(
                request,
                messages.SUCCESS,
                'your room has successfully been deleted!'
            )
    return redirect('home')


def delete_conversation(request, conversation_id):
    conversation = Conversations.objects.get(id=conversation_id)
    slug = conversation.room.slug
    conversation.delete()
    messages.add_message(
                request,
                messages.SUCCESS,
                'your conversation has successfully been deleted!'
            )
    return HttpResponseRedirect(reverse('in_room', args=[slug]))


def delete_comment(request, comment_id):
    comment = Comments.objects.get(id=comment_id)
    slug = comment.room.slug
    comment.delete()
    messages.add_message(
                request,
                messages.SUCCESS,
                'your comment has successfully been deleted!'
            )
    return HttpResponseRedirect(reverse('in_room', args=[slug]))
