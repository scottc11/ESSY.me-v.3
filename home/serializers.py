from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('pub_date', 'title', 'sub_title', 'body')
        # fields = '__all__'   # this will return all fields, including DB id
