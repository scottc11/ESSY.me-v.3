
from django.shortcuts import render, get_object_or_404
from django.contrib import admin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from home.models.project import Project
from home.models.social_media import SocialMediaAccount
from home.serializers import projectSerializer

# Create your views here.
def home(request):
    projects = Project.objects.order_by('pub_date')
    accounts = SocialMediaAccount.objects.all()
    context = { 'projects': projects, 'accounts': accounts }
    return render(request, 'home/home.html', context)


# ------ API --------
# list all projects or create a new one.
class projectsList(APIView):

    def get(self, request):
        projects = Project.objects.all()
        serializer = projectSerializer(projects, many=True)
        return Response(serializer.data)
    def post(self):
        pass
