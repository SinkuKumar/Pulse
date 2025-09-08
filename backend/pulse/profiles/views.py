from rest_framework import viewsets, permissions
from .models import Profile
from .serializers import ProfileSerializer


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission so only profile owner can edit their profile.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return all profiles (or just logged-in user’s profile if you prefer)
        return Profile.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)