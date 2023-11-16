from requests import Response
from rest_framework import generics, filters, status
from .models import Student
# from .permissions import CanUpdateStaffDetails, CanUpdateStudentDetails, IsAdminOrReadOnly
from .permissions import IsAdminOrReadOnly
from .serializers import StudentCreateSerializer, StudentUpdateSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
import logging
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

logger = logging.getLogger("main")

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
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
    
    def perform_list(self):
        try:
            pass
        except Exception as e:
            logger.error(f'Error performing list: {e}', exc_info=True)
        
class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentUpdateSerializer
    authentication_classes = [BasicAuthentication , SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    # def retrieve(self, request, *args, **kwargs):
    #     try:
    #         pass
    #     except ObjectDoesNotExist:
    #         return Response({'error': 'Resource not found'}, status=status.HTTP_404_NOT_FOUND)
    #     except Exception as e:
    #         logger.error(f'Error performing list: {e}', exc_info=True)
    #         return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
   
    def perform_destroy(self, instance):
        try:
            instance.delete()
        except ObjectDoesNotExist:
            return Response({'error': 'Resource not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f'Error deleting data: {e}', exc_info=True)
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)