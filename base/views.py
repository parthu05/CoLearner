from django.shortcuts import render, HttpResponse

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Room 1'},
    {'id': 2, 'name': 'Room 2'},
    {'id': 3, 'name': 'Room 3'},
]

def home(req):
    return render(req, 'home.html',{'rooms':rooms})

def room(req,pk):
    room = None
    for r in rooms:
        if r["id"] == int(pk):
            room = r
            break
    context = {'room':room}
    return render(req, 'room.html',context)