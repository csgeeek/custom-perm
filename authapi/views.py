from rest_framework.viewsets import ModelViewSet

from .permissions import CustomPermission
from .serializers import StudentModelSerializer
from .models import Student

# Create your views here.


class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    permission_classes = [CustomPermission]
