from rest_framework import permissions
from django.shortcuts import get_object_or_404
from .models import Event

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user or request.user.is_staff

class IsEventParticipant(permissions.BasePermission):
    def has_permission(self, request, view):
        event_id = view.kwargs.get('pk')
        slug = view.kwargs.get('slug')
        event = get_object_or_404(Event, pk=event_id, slug=slug)
        return request.user in event.participants.all()
        