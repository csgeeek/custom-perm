from rest_framework.permissions import BasePermission


class CustomPermission(BasePermission):
    """
    Allows Full access only to admin users.
    Allows SAFE_METHOD access to Non-staff users.
    """

    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True
        elif request.method in ('GET', 'HEAD', 'OPTIONS') and request.user.is_authenticated:
            return True
        return False
