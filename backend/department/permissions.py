from rest_framework import permissions

class IsAdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return super().has_permission(request, view)

# class CanUpdateStaffDetails(permissions.BasePermission):
#     message = "You do not have permission to update staff details."

#     def has_permission(self, request, view):
#         # Check if the user is authenticated
#         return request.user and request.user.is_authenticated

#     def has_object_permission(self, request, view, obj):
#         # Check if the user is an admin or non-teaching staff
#         return request.user.is_staff and obj.type_of_staff == 'non-teaching'

# class CanUpdateStudentDetails(permissions.BasePermission):
#     message = "You do not have permission to update student details."

#     def has_permission(self, request, view):
#         # Check if the user is authenticated
#         return request.user and request.user.is_authenticated

#     def has_object_permission(self, request, view, obj):
#         # Check if the user is an admin, teaching staff, or the student matching Student_Id
#         is_student = obj.Student_Id == request.user.username if hasattr(request.user, 'username') else False
#         is_teaching_staff = request.user.is_staff and request.user.type_of_staff == 'teaching'

#         return is_student or is_teaching_staff


