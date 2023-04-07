from rest_framework import permissions

# NOTE: make sure to add the BasePermission


class UpdateOwnProfile(permissions.BasePermission):

    # Will be called behind the scenes
    # https://detecttechnologies.udemy.com/course/django-python/learn/lecture/6955156#questions/6386372
    def has_object_permission(self, request, view, obj):
        """Allow users to edit their own profile"""

        # By default ModelViewset will allow any user to perform curd operation, but we need to restrict it
        if request.method in permissions.SAFE_METHODS:
            """Check if the user is trying to edit their own profile"""
            return True

        # obj is a reference to the object being modified,
        # request.user is referense to the user making the request, so if both are same then the user is trying to modify its own profile
        return obj.id == request.user.id


# need for this class, we get value error if we try to update the status when not authenticated
class UpdateOwnStatus(permissions.BasePermission):
    """allows users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        # if not SAFE_METHOD, then return true if the user is trying to update only their own userprofile
        # lecture 65
        # ? https://detecttechnologies.udemy.com/course/django-python/learn/lecture/6955156#questions/6386372
        # ?https://detecttechnologies.udemy.com/course/django-python/learn/lecture/6955156#questions/5526518
        return obj.user_profile.id == request.user.id
