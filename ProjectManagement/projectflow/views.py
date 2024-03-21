from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from account.models import User
def index(request):
    return render(request,"projectflow/index.html")

def about(request):
    return render(request,"projectflow/about.html")

def base(request):
    return render(request,"projectflow/base.html")

def alogin(request):
    return render(request,"projectflow/afterlogin.html")

def profile(request):
    return render(request,"projectflow/profile.html")


@login_required
def editprofile(request):
    if request.method == 'POST':
       
        user = request.user
        user.name = request.POST.get('name')
        user.email = request.POST.get('new_email')
        user.email = request.POST.get('confirm_email')

        user.save()
        
        return redirect('/')
    else:
        
        user = request.user

        return render(request, 'projectflow/editprofile.html', {'user': user})
