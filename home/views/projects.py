from django.shortcuts import render, get_object_or_404
from django.contrib import admin
from home.models.project import Project
from home.models.post import Post

def projects(request):
    projects = Project.objects.order_by('pub_date')
    return render(request, 'projects/projects.html', {'projects': projects})

def project(request, num):
    project = get_object_or_404(Project, pk=num)
    posts = Post.objects.filter(project=project)
    return render(request, 'projects/project.html', { 'project': project, 'posts': posts })
