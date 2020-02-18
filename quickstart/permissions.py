from rest_framework import permissions


class IsOnwerOrReadonly(permissions.BasePermission):
    """如果对象是该用户的，那么可以编辑，否则只能查看"""
    def has_object_permission(self, request, view, obj):
        """允许GET HEAD OPTIONS请求"""
        if request.method in permissions.SAFE_METHODS:
            return True
            
        return obj.owner == request.user