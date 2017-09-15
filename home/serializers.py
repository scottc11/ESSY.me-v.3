from rest_framework import serializers
from .models.project import Project

class projectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('pub_date', 'title', 'sub_title', 'body')
        # fields = '__all__'   # this will return all fields, including DB id
