from django.shortcuts import render, get_object_or_404
from django.contrib import admin
from blog.models import Entry

def blog(request):
    entries = Entry.objects.all()
    context = { 'entries': entries }
    return render(request, 'blog.html', context)

def entry_detail(request, id):
    entries = Entry.objects.all()
    entry = get_object_or_404(Entry, pk=id)
    context = {'entry': entry, 'entries': entries}
    return render(request, 'entry_detail.html', context)
