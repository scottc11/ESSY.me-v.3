
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from home.views.views import home, projects, project, post, kenobi
from blog.views import blog, entry_detail
from home.views.api import projectsList

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # BLOG
    url(r'^blog/$', blog, name='blog'),
    url(r'^blog/entries/(?P<id>[0-9])/$', entry_detail, name='entry_detail'),

    # PORTFOLIO
    url(r'^$', home, name='home'),
    url(r'^projects/$', projects, name="projects"),
    url(r'^projects/(?P<num>[0-9])/$', project, name="project"),
    url(r'^projects/(?P<prj>[0-9])/post/(?P<post>[0-9])/$', post, name="post"),
    url(r'^kenobi/', kenobi, name="kenobi"),

    url(r'^comments/', include('django_comments.urls')),

    url(r'^api/projects/', projectsList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
