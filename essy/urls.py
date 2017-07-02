
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from home.views import projectsList, home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^/', home),
    url(r'^projects/', projectsList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
