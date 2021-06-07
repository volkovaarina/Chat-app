from django.shortcuts import render, redirect
from datetime import datetime
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from .models import Room, Message


def home(request):
  return render(request, 'mysite/home.html')

def room(request, room):
  username = request.GET.get('username')
  room_details = Room.objects.get(name=room)
  return render(request, 'mysite/room.html', {
    'username': username,
    'room': room,
    'room_details': room_details

  })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']
    if Room.objects.filter(name=room).exists():
        return redirect('/room/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/room/'+room+'/?username='+username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id, date=timezone.now())
    new_message.save()
    return HttpResponse('Message sent successfully:)')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

def back(request):
  sed = request.session.get('username')
  return render(request, 'mysite/back.html')

  
#def rooms(request):
 # rooms = Room.objects.all()
  #return render(request, 'mysite/rooms.html', {'rooms' : rooms})


  #})
#def register(response):
#	if response.method == "POST":
#		form = UserCreationForm(response.POST)
#		if form.is_valid():
#			form.save()
#			return redirect('home')
#	else:
#		form = UserCreationForm()
		
	#return render(response, "register/register.html", {'form':form})

#def index(request):
 # return render(request,'mysite/index.html')
  #return HttpResponse(' <h1>Welcome!</h1><a href="/form">Регистрация</a>')

