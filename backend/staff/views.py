from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics, filters, status
from .models import Staff
from django.core.exceptions import ObjectDoesNotExist
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly
from .serializers import StaffCreateSerializer,StaffUpdateSerializer
import logging
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

logger = logging.getLogger(__name__)
class StaffList(generics.ListCreateAPIView, viewsets.ViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffCreateSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'type_of_staff', 'staff_id', 'department', 'created_by', 'created_at', 'modified_by', 'modified_at']
    search_fields = ['name', 'type_of_staff', 'staff_id', 'department', 'created_by', 'created_at', 'modified_by', 'modified_at']
    ordering_fields = ['name', 'type_of_staff', 'staff_id', 'department', 'created_by', 'created_at', 'modified_by', 'modified_at']

    def get(self, request, *args, **kwargs):
            try:
                queryset = Staff.objects.all()
                page = self.paginate_queryset(queryset)
                serializer = StaffCreateSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            except Exception as e:
                logger.error(f'Error retrieving Staff list: {e}', exc_info=True)
                return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
      
class StaffDetail(generics.RetrieveUpdateDestroyAPIView, viewsets.ViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffUpdateSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk, *args, **kwargs):
        try:
            instance = Staff.objects.get(id=pk)
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)  

        except ObjectDoesNotExist:
            return Response({'error': 'Staff not found'}, status=404)
        
        except Exception as e:
          
            logger.error(f'Error retrieving data: {e}', exc_info=True)
            return Response({'error': 'Internal Server Error'}, status=500)
        
    
    def delete(self, request, pk):
        try:
            st = Staff.objects.get(id=pk)
            st.delete()
            return Response({'success': 'Resource deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Staff.DoesNotExist:
            return Response({'error': 'Resource not found'}, status=404)
        except Exception as e:
            logger.error(f'Error deleting data: {e}', exc_info=True)
            return Response({'error': 'Internal Server Error'}, status=500)