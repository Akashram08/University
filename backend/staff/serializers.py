from rest_framework import serializers, status
from .models import Staff
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist  # Import ObjectDoesNotExist
import logging
from department.models import Department
logger = logging.getLogger(__name__)
class StaffCreateSerializer(serializers.ModelSerializer):
    created_by = serializers.SlugRelatedField(slug_field='username', read_only=True)
    modified_by = serializers.SlugRelatedField(slug_field='username', read_only=True)
    department = serializers.SlugRelatedField(slug_field='name', queryset=Department.objects.all(), many=True)
    staff_type_prefixes = {
        'non-teaching': 'ANT-',
        'teaching': 'AT-',
    }

    class Meta:
        model = Staff
        fields = '__all__'

    def create(self, validated_data):
        validated_data['name'] = validated_data['name'].title()
        validated_data['created_by'] = self.context['request'].user
        type_of_staff = validated_data.get('type_of_staff', '').lower()
        prefix = self.staff_type_prefixes.get(type_of_staff, '')
        validated_data['staff_id'] = prefix + validated_data['staff_id']
        validated_data['modified_at'] = None
        staff_id = validated_data['staff_id']
        existing_staff = Staff.objects.filter(staff_id=staff_id).first()
        if existing_staff:
            error_message = "A staff member with this staff ID already exists."
            logger.error(error_message)
            raise serializers.ValidationError(error_message, code=status.HTTP_400_BAD_REQUEST)

        return super().create(validated_data)

    def validate_Staff_Id(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("staff id must contain only numbers.", code=status.HTTP_400_BAD_REQUEST)
        return value

class StaffUpdateSerializer(serializers.ModelSerializer):
    created_by = serializers.SlugRelatedField(slug_field='username', read_only=True)
    modified_by = serializers.SlugRelatedField(slug_field='username', read_only=True)
    department = serializers.SlugRelatedField(slug_field='name', queryset=Department.objects.all(), many=True)
    class Meta:
        model = Staff
        fields = ['name', 'department', 'created_by', 'created_at', 'modified_by', 'modified_at']
    def update(self, instance, validated_data):
        user = self.context['request'].user
        validated_data['name'] = validated_data['name'].title()
        validated_data['modified_by'] = user
        validated_data['modified_at'] = timezone.now()
        try:
            instance = super().update(instance, validated_data)
        except Exception as e:
            logger.error(f'Error updating a staff: {e}', exc_info=True)
        return instance