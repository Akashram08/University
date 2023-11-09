from django.urls import path
from .import views
urlpatterns = [
    path('staffs/', views.StaffList.as_view(), name='staff-list-create'),
    path('staff/<int:pk>/', views.StaffDetail.as_view(), name='staff-retrieve-update-destroy'),
]