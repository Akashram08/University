from django.urls import path
from .import views

urlpatterns = [
    path('departments/', views.DepartmentList.as_view(), name='department-list-create'),
    path('department/<int:pk>/', views.DepartmentDetail.as_view(), name='department-retrieve-update-destroy'),
    path('university/<int:pk>/', views.University.as_view(), name='university-retrieve-update'),
]