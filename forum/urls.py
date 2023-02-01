from . import views
from django.urls import path

urlpatterns = [
    path('', views.RoomList.as_view(), name='home'),
    path('your_room', views.YourRoomList.as_view(), name='your_home'),
    path('<slug:slug>/', views.RoomView.as_view(), name='in_room'),
    path('add_room', views.addRoom.as_view(), name='add')
]
