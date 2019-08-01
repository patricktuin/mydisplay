from rest_framework import permissions

from displays.models import Display


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    # message ='fdssfadfd'

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.

        if request.method in permissions.SAFE_METHODS:
            display = Display.objects.get(serial_number=view.kwargs['serial_number'])
            if request.user == display.customer.user:
                return True

        # Write permissions are only allowed to the owner of the snippet.
        return False
