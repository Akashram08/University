from django.db import models
from django.contrib.auth.models import User
from department.models import Department

class Staff(models.Model):
    TEACHING ="Teaching"
    NONTEACHING="Non-teaching"
    name = models.CharField(max_length=100)
    type_of_staff_CHOICES = [(TEACHING,"Teaching staff"), (NONTEACHING,"Non Teaching staff")]
    type_of_staff= models.CharField(
        max_length=30,
        choices=type_of_staff_CHOICES,
        default=TEACHING )
    staff_id= models.CharField(unique=True, max_length=15)
    department = models.ManyToManyField(Department,  related_name='staff')
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='staff_created')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='staff_modified', null=True, blank= True)
    modified_at = models.DateTimeField( editable=False, null=True, blank=True)
    def __str__(self):
        return self.name
    
