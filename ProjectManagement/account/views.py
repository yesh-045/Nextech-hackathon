from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import User

def signup(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        if name and email and password1 and password2:
            user = User.objects.create_user(name, email, password1)
            print("User Created", user)
            return redirect('/login/')
        else:
            print("Something went wrong")
    else:
        print("Just show the form")
    return render(request, 'account/signup.html')

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        if email and password:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                print("User authenticated:", user)
                print("User logged in:", request.user)
                print( request.user.is_authenticated)
                return redirect("/alogin/")
    return render(request, 'account/login.html')
