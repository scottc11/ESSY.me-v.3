from django.shortcuts import render, get_object_or_404
from django.contrib import admin

from home.models.post import Post
from home.models.project import Project
from home.models.social_media import SocialMediaAccount
from home.models.technology import Technology

# Create your views here.
def home(request):
    projects = Project.objects.filter(featured=True)
    technologies = Technology.objects.all()
    accounts = SocialMediaAccount.objects.all()
    context = { 'projects': projects, 'accounts': accounts, 'technologies': technologies }
    return render(request, 'home.html', context)

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def project(request, num):
    accounts = SocialMediaAccount.objects.all()
    project = get_object_or_404(Project, pk=num)
    return render(request, 'project.html', { 'project': project, 'accounts': accounts })

def post(request, prj, post):
    project = get_object_or_404(Project, pk=prj)
    post = Post.objects.get(id=post, project=prj)
    return render(request, 'post.html', { 'project': project, 'post': post })
