from . import views
from django.urls import path


urlpatterns = [
    path('index/', views.index),
    path('activity/', views.activity),
    path('create-room/', views.create_room),
    path('delete/', views.delete),
    path('edit-user/', views.edit_user),
    path('login/', views.login),
    path('profile/', views.profile),
    path('room/', views.room),
    path('settings/', views.settings),
    path('signup/', views.signup),
    path('topics/', views.topics)
]