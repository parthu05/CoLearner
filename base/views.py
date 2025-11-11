from django.shortcuts import render, redirect
from .models import Room,Topic
from django.db.models import Q
from .forms import RoomForm, RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required
def home(req):
    q = req.GET.get('q') if req.GET.get('q') != None else ''

    rooms = Room.objects.filter(
        Q(name__icontains=q) | Q(topic__name__icontains=q) | Q(description__icontains=q) | Q(host__username__icontains=q)
    )

    topics = Topic.objects.all()
    rooms_count = rooms.count()
    context = {'rooms':rooms, 'topics':topics, 'rooms_count':rooms_count}
    return render(req, 'home.html', context)

@login_required
def room(req,pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(req, 'room.html',context)

@login_required
def createRoom(req):
    form = RoomForm()
    if req.method == 'POST':
        form = RoomForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(req, 'room_form.html',{'form':form})

@login_required
def updateRoom(req,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if req.method =='POST':
        form = RoomForm(req.POST, instance = room)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(req, 'room_form.html',{'form':form})

@login_required
def deleteRoom(req,pk):
    room = Room.objects.get(id=pk)
    if req.method == 'POST':
        room.delete()
        return redirect('home')
    return render(req, 'delete.html',{'obj':room})   

def registerView(req):
    form = RegistrationForm(req.POST or None)
    if req.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(req,user)
            messages.success(req, "Registration successful")
            return redirect('home')
        else:
            messages.error(req, "Unsuccessful registration. Invalid information.")
    return render(req, 'register.html',{'form':form})

def loginView(req):
    form = LoginForm(data=req.POST or None)
    if req.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(req,user)
            messages.success(req, "Login successful")
            return redirect('home')
        else:
            messages.error(req, "Invalid username or password")
    return render(req, 'login.html',{'form':form})

@login_required
def logoutView(req):
    logout(req)
    messages.info(req, "You have successfully logged out.") 
    return redirect('login')
