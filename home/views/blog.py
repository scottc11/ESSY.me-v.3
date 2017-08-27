from django.shortcuts import render, get_object_or_404
from django.contrib import admin
from home.models.blog.post import Post

def blog(request):
    print('something got here')
    posts = Post.objects.all()
    context = { 'posts': posts }
    return render(request, 'blog/blog.html', context)
