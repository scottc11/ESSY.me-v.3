from django.shortcuts import render, get_object_or_404
from django.contrib import admin
from home.models.project import Project
from home.models.post import Post

def projects(request):
    projects = Project.objects.order_by('pub_date')
    return render(request, 'projects/projects.html', {'projects': projects})

def project(request, num):
    print (request.META['HTTP_USER_AGENT'])
    project = get_object_or_404(Project, pk=num)
    return render(request, 'projects/project.html', { 'project': project })

def post(request, prj, post):
    project = get_object_or_404(Project, pk=prj)
    post = Post.objects.get(id=post, project=prj)
    return render(request, 'projects/post.html', { 'project': project, 'post': post })
