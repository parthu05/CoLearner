from django.shortcuts import render, redirect
from .models import Room,Topic
from django.db.models import Q
from .forms import RoomForm, RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(req):
    q = req.GET.get('q') if req.GET.get('q') != None else ''

    rooms = Room.objects.filter(
        Q(name__icontains=q) | Q(topic__name__icontains=q) | Q(description__icontains=q) | Q(host__username__icontains=q)
    )

    topics = Topic.objects.all()
    rooms_count = rooms.count()
    context = {'rooms':rooms, 'topics':topics, 'rooms_count':rooms_count}
    return render(req, 'home.html', context)

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

def registerView(req):
    form = RegistrationForm(req.POST or None)
    if req.method == 'POST':
        form = RegistrationForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req,user)
            return redirect('home')
    return render(req, 'register.html',{'form':form})
