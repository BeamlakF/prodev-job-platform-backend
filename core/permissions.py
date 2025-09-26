from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'


class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'user'


class IsOwnerOrReadOnly(BasePermission):
    """
    Object-level permission:
    - Owners can edit/delete their own objects.
    - Admins can edit everything.
    - Others can only read.
    """
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = GET, HEAD, OPTIONS → read-only allowed
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user
# Without IsOwnerOrReadOnly, any authenticated user could edit or delete another user’s job or application.
  
    
   