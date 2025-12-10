from rest_framework import permissions
class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        user=request.user
        if user.groups.filter(name='Admin').exists():
            return True
        return obj.owner==user