from django.db import models
from django.contrib.auth.models import User
# from student.models import Student
# from staff.models import Staff
class University(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='departments')
    
    def __str__(self):
        return self.name

