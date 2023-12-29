from rest_framework import permissions
from microblog.models.twits import Twits

from rest_framework import permissions


class IsAdminOrCreatorTwits(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        print('Here')
        if request.method in permissions.SAFE_METHODS:
            print('Here1')
            return True
        print('Here2')
        return request.user.is_authenticated and (request.user.is_staff or obj.user_id == request.user.id)
