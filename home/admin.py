from django.contrib import admin
from .models.project import Project
from .models.post import Post


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Post)
