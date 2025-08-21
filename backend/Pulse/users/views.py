from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserProfileUpdateSerializer, UserPasswordUpdateSerializer

# Update profile info
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileUpdateSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserProfileUpdateSerializer(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request):
        serializer = UserProfileUpdateSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# Update password
class UserPasswordChangeView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        serializer = UserPasswordUpdateSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.update(request.user, serializer.validated_data)
        return Response({"detail": "Password updated successfully"}, status=status.HTTP_200_OK)
