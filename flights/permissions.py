from rest_framework.permissions import BasePermission
import datetime

class IsOwner(BasePermission):
    message = "You must be the owner of this booking."

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        else:
            return False

class IsFuture(BasePermission):
    message = "Booking is in the past."

    def has_object_permission(self, request, view, obj):
        if obj.date >= datetime.date.today():
            return True
        else:
            return False            