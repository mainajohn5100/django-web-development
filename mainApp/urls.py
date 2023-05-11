from . import views
from django.urls import path


urlpatterns = [
    path('index.html/', views.index),
    path('activity.html/', views.activity),
    path('create-room.html/', views.create_room),
    path('delete.html/', views.delete),
    path('edit-user.html/', views.edit_user),
    path('login.html/', views.login),
    path('profile.html/', views.profile),
    path('room.html/', views.room),
    path('settings.html/', views.settings),
    path('signup.html/', views.signup),
    path('topics.html/', views.topics)
]