from unicodedata import name
from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name="home"),
    path('index/', views.index, name="index"),
    path('activity/', views.activity, name="activity"),
    path('create-room/', views.create_room, name="create-room"),
    path('delete/', views.delete, name="delete"),
    path('edit-user/', views.edit_user, name="edit-user"),
    path('login/', views.login, name="login"),
    path('profile/', views.profile, name="profile"),
    path('room/', views.room, name="room"),
    path('settings/', views.settings, name="settings"),
    path('signup/', views.signup, name="signup"),
    path('topics/', views.topics, name="topics")
]