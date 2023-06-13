from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request) -> None:
    return render(request, "mainApp/index.html")


def activity(request) -> None:
    return render(request, "mainApp/activity.html")
    
def create_room(request) -> None:
    return render(request, "mainApp/create-room.html")

def delete(request) -> None:
    return render(request, "mainApp/delete.html")

def edit_user(request) -> None:
    return render(request, "mainApp/edit-user.html")

def login(request) -> None:
    return render(request, "mainApp/login.html")

def profile(request) -> None:
    return render(request, "mainApp/profile.html")

def room(request) -> None:
    return render(request, "mainApp/room.html")

def settings(request) -> None:
    return render(request, "mainApp/settings.html")

def signup(request) -> None:
    return render(request, "mainApp/signup.html")

def topics(request) -> None:
    return render(request, "mainApp/topics.html")