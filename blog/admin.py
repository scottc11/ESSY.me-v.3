from django.contrib import admin
from blog.models import Entry, EntryImage
# Register your models here.

class ImageInlineAdmin(admin.TabularInline):
    model = EntryImage

class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ImageInlineAdmin]
    multiupload_form = True
    multiupload_list = False

admin.site.register(Entry, EntryAdmin)
