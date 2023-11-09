from rest_framework import generics, filters
# from .permissions import CanUpdateStaffDetails, CanUpdateStudentDetails, IsAdminOrReadOnly
from .permissions import IsAdminOrReadOnly
from .models import Department, University
from .serializers import DepartmentSerializer, UniversitySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
import logging

logger = logging.getLogger("main")


    
    # def perform_update(self, serializer):
    #     existing_object = self.get_object()

    #     # Check if modified_by is provided and not null
    #     if 'modified_by' in serializer.validated_data and serializer.validated_data['modified_by']:
    #         # Set modified_at when modified_by is not null
    #         serializer.save(modified_at=timezone.now())
    #     else:
    #         # Keep modified_at as is when modified_by is null
    #         serializer.validated_data['modified_at'] = existing_object.modified_at

class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    # permission_classes = [IsAdminOrReadOnly]
    permission_classes= [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']
    def perform_create(self, serializer):
        try:
            serializer.save() 
        except Exception as e:
            logger.error(f'Error creating a department: {e}', exc_info=True)

class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAdminOrReadOnly]


class University(generics.RetrieveUpdateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [IsAdminOrReadOnly]
