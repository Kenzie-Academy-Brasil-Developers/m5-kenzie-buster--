from rest_framework import permissions
from rest_framework.views import Request, View


class MoviesDetailsPermission(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        if request.method == 'DELETE':
            return request.user.is_employee
        return request.method in permissions.SAFE_METHODS

class MoviesPermission(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        if request.method == 'POST':
            return request.user.is_employee
        return request.method in permissions.SAFE_METHODS
