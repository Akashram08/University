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

logger = logging.getLogger("main")
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
                serializer = StaffCreateSerializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)

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
            # instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)  

        except Staff.DoesNotExist:
            return Response({'error': 'Resource not found'}, status=404)
        
        except Exception as e:
          
            logger.error(f'Error retrieving data: {e}', exc_info=True)
            return Response({'error': 'Internal Server Error'}, status=500)
        
    
    def delete(self, request, pk):
        try:
            st = Staff.objects.get(id=pk)
            st.delete()
        except Staff.DoesNotExist:
            return Response({'error': 'Resource not found'}, status=404)
        except Exception as e:
            logger.error(f'Error deleting data: {e}', exc_info=True)
            return Response({'error': 'Internal Server Error'}, status=500)