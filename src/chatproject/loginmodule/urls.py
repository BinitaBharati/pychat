from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
	#Need to use dumbEntry, else control will go to login method of view
    path('<dumbEntry>/', views.logout, name='logout'),
]
