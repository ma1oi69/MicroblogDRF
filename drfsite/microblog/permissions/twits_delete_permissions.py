from rest_framework import permissions
from microblog.models.twits import Twits


class IsAdminOrCreatorDelete(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        true_creator = Twits.objects.filter(user_id=request.user.id).exists()
        if true_creator:
            return bool(request.user and request.user.is_staff) or true_creator
