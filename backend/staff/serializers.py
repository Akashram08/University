from rest_framework import serializers, status
from .models import Staff
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist  # Import ObjectDoesNotExist
import logging

logger = logging.getLogger("main")
class StaffCreateSerializer(serializers.ModelSerializer):
    created_by = serializers.SlugRelatedField(slug_field='username', read_only=True)
    modified_by = serializers.SlugRelatedField(slug_field='username', read_only=True)
   
    staff_type_prefixes = {
        'non-teaching': 'ANT-',
        'teaching': 'AT-',
    }

    class Meta:
        model = Staff
        fields = '__all__'

    def create(self, validated_data):
        validated_data['name'] = validated_data['name'].title()

        type_of_staff = validated_data.get('type_of_staff', '').strip().lower()
        prefix = self.staff_type_prefixes.get(type_of_staff, '')
        validated_data['staff_id'] = prefix + validated_data['staff_id']
        validated_data['modified_at'] = None
        staff_id = validated_data['staff_id']
        try:
            existing_staff = Staff.objects.get(staff_id=staff_id)
            raise serializers.ValidationError("A staff member with this staff ID already exists.", code=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            pass
        return super().create(validated_data)

    def validate_Staff_Id(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("staff id must contain only numbers.", code=status.HTTP_400_BAD_REQUEST)
        return value

class StaffUpdateSerializer(serializers.ModelSerializer):
    created_by = serializers.SlugRelatedField(slug_field='username', read_only=True)
    modified_by = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Staff
        fields = ['name', 'department', 'created_by', 'created_at', 'modified_by', 'modified_at']
    def update(self, instance, validated_data):
        user = self.context['request'].user
        validated_data['name'] = validated_data['name'].capitalize()
        validated_data['modified_by'] = user
        validated_data['modified_at'] = timezone.now()
        try:
            instance = super().update(instance, validated_data)
        except Exception as e:
            logger.error(f'Error updating a staff: {e}', exc_info=True)
        return instance