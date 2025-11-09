from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

# Create your views here.

def home(req):
    rooms = Room.objects.all()
    return render(req, 'home.html',{'rooms':rooms})

def room(req,pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(req, 'room.html',context)

def createRoom(req):
    form = RoomForm()
    if req.method == 'POST':
        form = RoomForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(req, 'room_form.html',{'form':form})

def updateRoom(req,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if req.method =='POST':
        form = RoomForm(req.POST, instance = room)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(req, 'room_form.html',{'form':form})

def deleteRoom(req,pk):
    room = Room.objects.get(id=pk)
    if req.method == 'POST':
        room.delete()
        return redirect('home')
    return render(req, 'delete.html',{'obj':room})   
