from django.contrib import admin
from .models.projects.project import Project
from .models.blog.post import Post

# Register your models here.
admin.site.register(Project)
admin.site.register(Post)
