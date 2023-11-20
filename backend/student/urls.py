from django.urls import path
from .import views
urlpatterns = [
    path('students/', views.StudentList.as_view({'get':'get'}), name='student-list-create'),
    path('student/<pk>', views.StudentDetail.as_view({'delete': 'delete', 'get': 'get'}), name='student-retrieve-update-destroy'),
]