from rest_framework.permissions import BasePermission
import datetime

class IsOwner(BasePermission):
    message = "You must be the owner of this booking."

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user or request.user.is_staff:
            return True
        else:
            return False

class IsFuture(BasePermission):
    message = "Booking can't be updated unless it was 3 days away"

    def has_object_permission(self, request, view, obj):
        days_left = (obj.date - datetime.date.today()).days
        if days_left > 3:
            return True
        else:
            return False            