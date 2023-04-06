from rest_framework import permissions

# NOTE: make sure to add the BasePermission


class UpdateOwnProfile(permissions.BasePermission):

    # Will be called behind the scenes
    def has_object_permission(self, request, view, obj):
        """Allow users to edit their own profile"""

        # By default ModelViewset will allow any user to perform curd operation, but we need to restrict it
        if request.method in permissions.SAFE_METHODS:
            """Check if the user is trying to edit their own profile"""
            return True

        # obj is a reference to the object being modified,
        # request.user is referense to the user making the request, so if both are same then the user is trying to modify its own profile
        return obj.id == request.user.id
