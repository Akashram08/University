from rest_framework import generics, filters
from .models import Student
# from .permissions import CanUpdateStaffDetails, CanUpdateStudentDetails, IsAdminOrReadOnly
from .permissions import IsAdminOrReadOnly
from .serializers import StudentCreateSerializer, StudentUpdateSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
import logging
from rest_framework.authentication import BasicAuthentication

logger = logging.getLogger("main")

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'CGPA', 'student_id', 'department', 'created_by', 'created_at', 'modified_by', 'modified_at']
    search_fields = ['name', 'CGPA', 'student_id', 'department', 'created_by', 'created_at', 'modified_by', 'modified_at']
    ordering_fields = ['name', 'CGPA', 'student_id', 'department', 'created_by', 'created_at', 'modified_by', 'modified_at']

    def perform_create(self, serializer):
        try:
            serializer.save(created_by=self.request.user)
        except Exception as e:
            logger.error(f'Error creating a staff: {e}', exc_info=True)
        
class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentUpdateSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
   
 