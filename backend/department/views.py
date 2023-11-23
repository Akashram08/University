from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics, filters, status
from .permissions import IsAdminOrReadOnly
from .models import Department, University
from .serializers import DepartmentSerializer, UniversitySerializer
from django_filters.rest_framework import DjangoFilterBackend
import logging
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

logger = logging.getLogger(__name__)


class DepartmentList(generics.ListCreateAPIView, viewsets.ViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name'] 

    def get(self, serializer):
        try:
            queryset = Department.objects.all()
            page = self.paginate_queryset(queryset)
            serializer = DepartmentSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            logger.error(f'Error retrieving Department list: {e}', exc_info=True)
            return Response({'error': 'Internal Server Error'},  status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    

    

class University(generics.RetrieveUpdateAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAdminOrReadOnly]