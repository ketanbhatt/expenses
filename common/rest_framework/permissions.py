from rest_framework import permissions


class IsOwnerEditingObject(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    owner_field_name = "user"

    def has_object_permission(self, request, view, obj):
        return getattr(obj, self.owner_field_name) == request.user
