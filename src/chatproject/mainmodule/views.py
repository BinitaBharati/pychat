from django.http import HttpResponse
from django.shortcuts import render
from mainmodule.models import Chatroom
from django.core import serializers
from django.http import JsonResponse
from django.utils.safestring import mark_safe
import json


def home(request):
    #return HttpResponse("Hello, world. You're at chatproject home.")
    for key, value in request.session.items():
    	print('{} => {}'.format(key, value))
    sessionUser = request.session.get('user', 'none')
    sessionUserEmail = request.session.get('userEmail', 'none')
    sessionUserAdmin = request.session.get('type', 'none')
    print ("main: sessionUser = "+sessionUser + " "+sessionUserEmail)
	#Why do we need to put back in session what is already there , huh ?
    request.session['user'] = sessionUser
    request.session['userEmail'] = sessionUserEmail
    request.session['type'] = sessionUserAdmin
    return render(request, 'mainmodule/home.html', {"userName" : sessionUser, "userEmail" : sessionUserEmail})
    #else:
            #return HttpResponse("Please enable cookies and try again.")

def chatrooms(request):
    chatrooms = Chatroom.objects.all()
    return JsonResponse(serializers.serialize('json', chatrooms), safe=False)
    #else:dbUser = Login.objects.get(email = userEmail)
            #return HttpResponse("Please enable cookies and try again.")

def joinchatroom2(request, chatroomname):
     return render(request, 'mainmodule/room.html', {
        'room_name_json': mark_safe(json.dumps(chatroomname))
    })

def joinchatroom(request, chatroomname):
     #return JsonResponse(serializers.serialize('json', {'room_name_json' : chatroomname}), safe=False)
     print ("why u calling me")
     return JsonResponse({'room' : chatroomname}, safe=False)