from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allows Users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to edittheir own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
