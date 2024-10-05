from rest_framework import permissions


class MyIsAuthenticated(permissions.BasePermission):
    message = 'You don\'t have any permission to see post lists'

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


class IsAnnaPermission(permissions.BasePermission):
    message = 'Test'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.user == request.user and request.user.username == 'anna':
            if request.method in ['PUT', 'PATCH']:
                return False

            return True

        return obj.user == request.user
