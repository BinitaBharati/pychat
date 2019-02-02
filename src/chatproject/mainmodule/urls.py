from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all/', views.chatrooms, name='chatrooms'),
#path('chatroom2/<chatroomname>', views.joinchatroom2, name='joinchatroom2'),
    path('<chatroomname>/', views.joinchatroom, name='joinchatroom'),
    ]
