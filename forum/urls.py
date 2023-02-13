from . import views
from django.urls import path

urlpatterns = [
    path('', views.RoomList.as_view(), name='home'),
    path('your_room', views.YourRoomList.as_view(), name='your_home'),
    path('<slug:slug>/', views.RoomView.as_view(), name='in_room'),
    path('delete_room/<room_id>', views.delete_room, name='delete'),
    path('delete_conversation/<conversation_id>', views.delete_conversation, name='delete_conversation'),
    path('edit_conversation/<conversation_id>', views.edit_conversation.as_view(), name='edit'),
]
