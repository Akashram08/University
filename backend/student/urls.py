from django.urls import path
from .import views
urlpatterns = [
    path('students/', views.StudentList.as_view(), name='student-list-create'),
    path('student/<int:pk>/', views.StudentDetail.as_view(), name='student-retrieve-update-destroy'),
]