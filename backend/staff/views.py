from requests import Response
from rest_framework import generics, filters
from .models import Staff
# from .permissions import CanUpdateStaffDetails, CanUpdateStudentDetails, IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly
from .serializers import StaffCreateSerializer,StaffUpdateSerializer
import logging
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

logger = logging.getLogger("main")
class StaffList(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffCreateSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'type_of_staff', 'staff_id', 'department', 'created_by', 'created_at', 'modified_by', 'modified_at']
    search_fields = ['name', 'type_of_staff', 'staff_id', 'department', 'created_by', 'created_at', 'modified_by', 'modified_at']
    ordering_fields = ['name', 'type_of_staff', 'staff_id', 'department', 'created_by', 'created_at', 'modified_by', 'modified_at']

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


    
      
class StaffDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffUpdateSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
  
    def retrieve(self, staff_id):
       
        try:
            instance = Staff.objects.get(staff_id=staff_id)
            serializer = StaffUpdateSerializer(instance)
            return Response(serializer.data)
        except StaffUpdateSerializer.DoesNotExist:
            return Response({'error': 'Resource not found'}, status=404)
        except Exception as e:
            logger.error(f'Error retrieving data: {e}', exc_info=True)
            return Response({'error': 'Internal Server Error'}, status=500)
    
    def perform_destroy(self, instance):
        try:
            instance.delete()
        except Exception as e:
            logger.error(f'Error deleting data: {e}', exc_info=True)
            return Response({'error': 'Internal Server Error'}, status=500)
