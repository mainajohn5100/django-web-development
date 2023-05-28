from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request) -> None:
    return render(request, "mainApp/theme/index.html")


def activity(request) -> None:
    return render(request, "mainApp/theme/activity.html")
    
def create_room(request) -> None:
    return render(request, "mainApp/theme/create-room.html")

def delete(request) -> None:
    return render(request, "mainApp/theme/delete.html")

def edit_user(request) -> None:
    return render(request, "mainApp/theme/edit-user.html")

def login(request) -> None:
    return render(request, "mainApp/theme/login.html")

def profile(request) -> None:
    return render(request, "mainApp/theme/profile.html")

def room(request) -> None:
    return render(request, "mainApp/theme/room.html")

def settings(request) -> None:
    return render(request, "mainApp/theme/settings.html")

def signup(request) -> None:
    return render(request, "mainApp/theme/signup.html")

def topics(request) -> None:
    return render(request, "mainApp/theme/topics.html")