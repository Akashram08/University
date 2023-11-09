from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('department.urls')),
    path('api/v1/', include('staff.urls')),
    path('api/v1/', include('student.urls')),
   
]
