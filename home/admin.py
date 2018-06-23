from django.contrib import admin
from .models.project import Project
from .models.post import Post
from .models.technology import Technology
from .models.social_media import SocialMediaAccount
from .models.image import Image

class ImageInlineAdmin(admin.TabularInline):
    model = Image


class PostInline(admin.TabularInline):
    model = Post


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ImageInlineAdmin]
    multiupload_form = True
    multiupload_list = False

# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Technology)
admin.site.register(SocialMediaAccount)
