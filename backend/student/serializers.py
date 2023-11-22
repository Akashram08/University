from rest_framework import serializers, status
from .models import Student
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist  # Import ObjectDoesNotExist
import logging
from department.models import Department
logger = logging.getLogger(__name__)


        
class StudentCreateSerializer(serializers.ModelSerializer):
    created_by = serializers.SlugRelatedField(slug_field='username', read_only=True)
    modified_by = serializers.SlugRelatedField(slug_field='username', read_only=True)
    department = serializers.SlugRelatedField(slug_field='name', queryset=Department.objects.all())

    class Meta:
        model = Student
        fields = '__all__'

    def first_letters(self,validated_data):
        dep=validated_data['department']
        if isinstance(dep, Department):
            # Assuming 'name' is the attribute of Department containing the string
            dep_name = dep.name
        else:
            dep_name = dep

        words = dep_name.split()
    

# Extract the first letter of each word
        first_letters = [word[0] for word in words if word.istitle()]

# Combine the first letters into a new string
        secondprefix = ''.join(first_letters)
        return secondprefix
    def create(self, validated_data):
        secondprefix = self.first_letters(validated_data)
        validated_data['name'] = validated_data['name'].title()
        # Add the fixed prefix 'AM-' to the Student_Id during creation
        validated_data['student_id'] = 'AM-' + secondprefix +validated_data['student_id']
        validated_data['modified_at'] = None
        validated_data['created_by'] = self.context['request'].user
        student_id = validated_data['student_id']
        existing_student = Student.objects.filter(student_id=student_id).first()
        if existing_student:
            error_message = "A student member with this student ID already exists."
            logger.error(error_message)
            raise serializers.ValidationError(error_message, code=status.HTTP_400_BAD_REQUEST)

        return super().create(validated_data)

    def validate_CGPA(self, value):
        cgpa_str = str(value)  # Convert CGPA to a string
        if not cgpa_str.replace('.', '', 1).isdigit():
            raise serializers.ValidationError("CGPA must be a valid numeric value.", code=status.HTTP_400_BAD_REQUEST)
        return value

    def validate_student_id(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Student ID must contain only numbers.", code=status.HTTP_400_BAD_REQUEST)
        return value

class StudentUpdateSerializer(serializers.ModelSerializer):
    created_by = serializers.SlugRelatedField(slug_field='username', read_only=True)
    modified_by = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Student
        fields = ['name', 'CGPA', 'created_by', 'created_at', 'modified_by', 'modified_at']
    def update(self, instance, validated_data):
        user = self.context['request'].user
        validated_data['name'] = validated_data['name'].title()
        validated_data['modified_by'] = user
        validated_data['modified_at'] = timezone.now()
        try:
            instance = super().update(instance, validated_data)
        except ObjectDoesNotExist as e:
            logger.error(f'ObjectDoesNotExist exception: {e}', exc_info=True)
            raise serializers.ValidationError("Object does not exist", code=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f'Error updating a student: {e}', exc_info=True)
        return instance
    
