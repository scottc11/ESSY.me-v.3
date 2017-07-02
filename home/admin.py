from django.shortcuts import get_object_or_404
from django.contrib import admin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Project
from .serializers import ProjectSerializer

# Register your models here.
admin.site.register(Project)
