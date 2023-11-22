from rest_framework import serializers, status
from .models import University, Department
import logging
logger = logging.getLogger(__name__)
class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):

    staff_count = serializers.ReadOnlyField()
    student_count = serializers.ReadOnlyField()
    university = serializers.SlugRelatedField(slug_field='name', queryset=University.objects.all())
    class Meta:
        model = Department
        fields = '__all__'
    def create(self, validated_data):
        department_name = validated_data['name']
        existing_staff = Department.objects.filter(name=department_name).first()
        if existing_staff:
            error_message = "The department with the same name already exists."
            logger.error(error_message)
            raise serializers.ValidationError(error_message, code=status.HTTP_400_BAD_REQUEST)

        return super().create(validated_data)
