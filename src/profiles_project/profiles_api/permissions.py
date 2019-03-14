from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allows Users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class PostOwnStatus(permissions.BasePermission):
    """Allow Users to update their own status"""

    def has_object_permission(seld, request, view, obj):
        """Check if user is trying to update their own status"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
