from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Project


@login_required
def list(request):
    project=Project.objects.filter(created_by=request.user)
    return render(request,'project/list.html',{
        'projects' :project
    })

@login_required
def add_project(request):
    if request.method == "POST":
        name=request.POST.get('name','')
        description=request.POST.get("description",'')
        if name:
            projects=Project.objects.create(name=name,description=description,created_by=request.user)
            return redirect("/project/list/")
        else:
            print("NOT Valid")
    return render(request,'project/add.html')
    
@login_required
def details(request,pk):
    details=Project.objects.filter(created_by=request.user).get(pk=pk)
    return render(request,'project/details.html',{
        'projects' :details
    })
@login_required
def edit_project(request,pk):
    details=Project.objects.filter(created_by=request.user).get(pk=pk)
    if request.method == "POST":
        name=request.POST.get('name','')
        description=request.POST.get("description",'')
        if name:
           details.name=name
           details.description=description
           details.save()
           return redirect("/project/list/")
    return render(request,'project/edit.html',{
        'projects' :details
    })
@login_required
def delete_project(request,pk):
    details=Project.objects.filter(created_by=request.user).get(pk=pk)
    details.delete()
    return redirect("/project/list/")
