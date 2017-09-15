
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from home.views.views import projectsList, home
from home.views.blog import blog, post_detail
from home.views.projects import projects

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^blog/$', blog, name='blog'),
    url(r'^posts/(?P<post_id>[0-9]+)/$', post_detail, name="post_detail"),
    url(r'^projects/$', projects, name='projects'),

    url(r'^api/projects/', projectsList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
