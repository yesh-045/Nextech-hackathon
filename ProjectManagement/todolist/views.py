from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Todolist
from project.models import Project

@login_required
def add(request, project_id):
    try:
        project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    
    if request.method == "POST":
        name = request.POST.get('name', '')  # Get the 'name' field from form data
        description = request.POST.get("description", '')
        if name:  # Check if 'name' is not empty
        
            todolist = Todolist.objects.create(project=project, name=name, description=description, created_by=request.user)
            return redirect(f'/project/{project_id}/details/')
    
    return render(request, 'todolist/add.html', {'project': project})
