from rest_framework.response import Response
from rest_framework import generics, filters, status
from rest_framework import viewsets
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

class StudentList(generics.ListCreateAPIView, viewsets.ViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'CGPA', 'student_id', 'department', 'created_by', 'created_at', 'modified_by', 'modified_at']
    search_fields = ['name', 'CGPA', 'student_id', 'department', 'created_by', 'created_at', 'modified_by', 'modified_at']
    ordering_fields = ['name', 'CGPA', 'student_id', 'department', 'created_by', 'created_at', 'modified_by', 'modified_at']

    

    
        
class StudentDetail(generics.RetrieveUpdateDestroyAPIView, viewsets.ViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentUpdateSerializer
    authentication_classes = [BasicAuthentication , SessionAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'  
    
    def get(self, request, pk, *args, **kwargs):
        try:
            instance = Student.objects.get(id=pk)
            # instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)  

        except Student.DoesNotExist:
            return Response({'error': 'Resource not found'}, status=404)
        
        except Exception as e:
            # Log the error or handle it as needed
            logger.error(f'Error retrieving data: {e}', exc_info=True)
            return Response({'error': 'Internal Server Error'}, status=500)
        
    def delete(self, request, pk):
        try:
            st = Student.objects.get(id=pk)
            st.delete()
        except Student.DoesNotExist:
            return Response({'error': 'Resource not found'}, status=404)
        except Exception as e:
            logger.error(f'Error deleting data: {e}', exc_info=True)
            return Response({'error': 'Internal Server Error'}, status=500)