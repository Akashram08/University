from django.urls import path
from .import views
urlpatterns = [
    path('staffs/', views.StaffList.as_view({'get':'get'}), name='staff-list-create'),
    path('staff/<pk>', views.StaffDetail.as_view({'delete':'delete','get':'get'}), name='staff-retrieve-update-destroy'),
]