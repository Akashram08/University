from django.db import models
from django.contrib.auth.models import User
from department.models import Department

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id= models.CharField(unique=True, max_length=10)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, related_name='students')
    CGPA = models.DecimalField(max_digits=3, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='students_created')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='students_modified', null=True, blank= True)
    modified_at = models.DateTimeField(editable=False, null=True, blank= True)

    def __str__(self):
        return self.name   
    
    

