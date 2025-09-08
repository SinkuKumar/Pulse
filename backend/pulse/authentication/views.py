from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class CookieTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            data = response.data
            refresh = data.get("refresh")
            access = data.get("access")

            # Set HttpOnly cookies
            response.set_cookie(
                key="access",
                value=access,
                httponly=True,
                secure=True,       # ✅ only send via HTTPS
                samesite="Strict", # or "Lax" depending on frontend/backend setup
                max_age=300,       # 5 minutes
            )
            response.set_cookie(
                key="refresh",
                value=refresh,
                httponly=True,
                secure=True,
                samesite="Strict",
                max_age=7*24*60*60, # 7 days
            )
        return response


class CookieTokenRefreshView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get("refresh")
        if refresh_token is None:
            return Response({"detail": "No refresh token"}, status=400)

        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)
        except Exception:
            return Response({"detail": "Invalid refresh token"}, status=400)

        response = Response({"access": access_token})
        response.set_cookie(
            key="access",
            value=access_token,
            httponly=True,
            secure=True,
            samesite="Strict",
            max_age=300,
        )
        return response


class LogoutView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get("refresh")
        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
            except Exception:
                pass

        response = Response({"detail": "Logged out"})
        response.delete_cookie("access")
        response.delete_cookie("refresh")
        return response
