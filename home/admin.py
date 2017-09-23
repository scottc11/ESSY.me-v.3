from django.contrib import admin
from .models.project import Project
from .models.post import Post
from .models.technology import Technology
from .models.social_media import SocialMediaAccount

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Post)
admin.site.register(Technology)
admin.site.register(SocialMediaAccount)
