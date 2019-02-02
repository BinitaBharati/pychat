from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from loginmodule.models import Login


@csrf_exempt
def login(request):
    print ("buhuuu")
    for key in request.POST:
    	print(key)
    	value = request.POST[key]
    	print(value)
    userEmail = request.POST.get("inputEmail","")
    userPassword = request.POST.get("inputPassword","")
    isAdminCheck = request.POST.get("isAdminCheck","")
    type = 'user'
    if isAdminCheck == 'on':
         type = 'admin'
    try:
    # get your models
           dbUser = Login.objects.get(email = userEmail)
           if dbUser.password == userPassword:
              request.session['user'] = dbUser.name
              request.session['userEmail'] = dbUser.email
              request.session['type'] = dbUser.type
              print ("db user email "+dbUser.email)
              curUser = request.session.get('user', 'none')
              curUserEmail = request.session.get('userEmail', 'none')
              print ("printing session data "+curUser + " " +curUserEmail)
              return render(request, 'mainmodule/home.html', {"userName" : dbUser.name, "userEmail" : dbUser.email})
           else:
              return render(request, 'mainmodule/loginerror.html')
    except Login.DoesNotExist:
    # do something
           return render(request, 'mainmodule/loginerror.html')
		  
		  
		  
def logout(request, dumbEntry):
       print ("logout entered")
       curUser = request.session.get('user', 'none')
       curUserEmail = request.session.get('userEmail', 'none')
       print ("logout: curUser = "+curUser + ", curUserEmail = "+curUserEmail)
       request.session['user'] = 'none'
       request.session['userEmail'] = 'none'
       request.session['type'] = 'none'
       return render(request, 'mainmodule/home.html')

