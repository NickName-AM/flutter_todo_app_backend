from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Only owner of the object can modify/delete the object
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user