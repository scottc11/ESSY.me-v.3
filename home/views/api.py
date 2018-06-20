
from rest_framework.views import APIView
from rest_framework.response import Response
from home.serializers import projectSerializer
from home.models.project import Project


# ------ API --------
# list all projects or create a new one.
class projectsList(APIView):

    def get(self, request):
        projects = Project.objects.all()
        serializer = projectSerializer(projects, many=True)
        return Response(serializer.data)
    def post(self):
        pass
