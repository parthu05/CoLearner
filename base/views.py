from django.shortcuts import render, HttpResponse
from .models import Room

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Room 1'},
    {'id': 2, 'name': 'Room 2'},
    {'id': 3, 'name': 'Room 3'},
]

def home(req):
    rooms = Room.objects.all()
    return render(req, 'home.html',{'rooms':rooms})

def room(req,pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(req, 'room.html',context)