from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request) -> None:
    return render(request, 'theme/index.html')


def activity(request) -> None:
    return render(request, 'theme/activity.html')
    
def create_room(request) -> None:
    return render(request, 'theme/create-room.html')

def delete(request) -> None:
    return render(request, 'theme/delete.html')

def edit_user(request) -> None:
    return render(request, 'theme/edit-user.html')

def login(request) -> None:
    return render(request, 'theme/login.html')

def profile(request) -> None:
    return render(request, 'theme/profile.html')

def room(request) -> None:
    return render(request, 'theme/room.html')

def settings(request) -> None:
    return render(request, 'theme/settings.html')

def signup(request) -> None:
    return render(request, 'theme/signup.html')

def topics(request) -> None:
    return render(request, 'theme/topics.html')