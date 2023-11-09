from rest_framework import serializers
from .models import University, Department

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    # staff_count = serializers.SerializerMethodField()
    # student_count = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = '__all__'

    # def get_staff_count(self, obj):
    #     return obj.staff_count()

    # def get_student_count(self, obj):
    #     return obj.student_count()
    
