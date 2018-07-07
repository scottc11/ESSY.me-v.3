
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from home.views.views import home, projects, project, post, kenobi
from home.views.blog import blog, post_detail
from home.views.api import projectsList

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^blog/$', blog, name='blog'),
    url(r'^posts/(?P<post_id>[0-9]+)/$', post_detail, name="post_detail"),
    url(r'^projects/$', projects, name="projects"),
    url(r'^projects/(?P<num>[0-9])/$', project, name="project"),
    url(r'^projects/(?P<prj>[0-9])/post/(?P<post>[0-9])/$', post, name="post"),
    url(r'^kenobi/', kenobi, name="kenobi"),

    url(r'^api/projects/', projectsList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
