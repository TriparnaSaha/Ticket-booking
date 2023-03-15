from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.http import HttpResponse
from .models import Destination
from .models import booking


def index(request):
    return render(request, "index.html")

def customer(request):
    return render(request, "customer.html")


def home(request):
    return render(request, "home.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/home')
        else:
            return HttpResponse('<script>alert("Login error..!!")</script>')


def custsignup(request):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        uname = request.POST['username']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if pass1 == pass2:
            user = User.objects.create_user(first_name=fname, last_name=lname, email=email, username=uname, password=pass1)
            user.save()
            return redirect('/customer')
    else:
        return render(request, "custsignup.html")

def flightinfo(request):
    return render(request, "flightinfo.html")




def logout(request):
    auth.logout(request, user)
    return redirect('/customer')

    
    
