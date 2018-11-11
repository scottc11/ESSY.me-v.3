from django.shortcuts import render, get_object_or_404
from django.contrib import admin
from blog.models import Entry

def blog(request):
    entries = Entry.objects.all()
    context = { 'entries': entries }
    return render(request, 'blog.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post.html', {'post': post})
