from django.shortcuts import render, get_object_or_404
from django.contrib import admin
from home.models.project import Project

def projects(request):
    projects = Project.objects.order_by('pub_date')
    return render(request, 'projects/projects.html', {'projects': projects})

def project(request, num):
    project = get_object_or_404(Project, pk=num)
    return render(request, 'projects/project.html', {'project': project})
