#from django.db import models
#from django.http.response import Http404
from django.contrib import auth
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from django.contrib.auth.models import User
from web_app.models import ContactModel
from django.contrib import messages
from django.contrib.auth import authenticate ,login ,logout
#from blog.models import Post
#from .models import Contact


# Create your views here.
def index(request):
  return render(request, 'index.html')
 # return  HttpResponse("this is Home page")
def about(request):
  return render(request, 'about.html')
  
def services(request):
  return render(request, 'services.html')


def contact(request):
  if request.method == "POST":
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    desc = request.POST.get('desc')


    save=ContactModel(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
    save.save()
    messages.success(request, 'Your form submited Sucessfully!')
  return render(request, "contact.html")  


  
def handelsignup(request):
  if request.method == "POST":
    #get the post parameter
    Username=request.POST['Username']
    fname=request.POST['fname']
    lname=request.POST['lname']
    email=request.POST['email']
    password1=request.POST['password1']
    password2=request.POST['password2']

            
  #check for invalid input in form  
    
    #checking username leangth
    if len(Username)<10 or len(fname)>10 or len(lname)>10 or len(email)>10:
      messages.error(request, "Please Form fill up properlly!")
      return redirect('web_app')
    
    #chacking username alfanumerinc
    if not Username.isalnum():
      messages.error(request, "User name should be letter and number only")
      return redirect('web_app')

    #checking username password
    if (password1!=password2):
      messages.error(request, "your password do not maching")
      return redirect('web_app')
    


  #Create Users 
    
    myuser=User.objects.create_user(Username, email, password1)
    myuser.first_name=fname
    myuser.last_name=lname
    myuser.save()
    # printing in message
    messages.success(request, "Your SignUp has Successfully Completed")
    return redirect('web_app')
  
  else:
    return HttpResponse('404- something went wrong')

#for login 
def handellogin(request):
  if request.method == "POST":
    loginUsername=request.POST['loginUsername']
    loginpassword=request.POST['loginpassword']

    user=authenticate(username= loginUsername, password= loginpassword)

    if user is not None:
      login(request, user)
      messages.success(request, "you are successfully loged in")
      return redirect("web_app")
    else:
      messages.error(request, "Invalid Credentials! Please try again")
      return redirect("web_app")

  else:
    return HttpResponse("404 - Not found dont try to be oversmart")




#for logout 
def handellogout(request):
  logout(request)
  messages.success(request, "Successfully logged out")
  return redirect('web_app')
   


    
       