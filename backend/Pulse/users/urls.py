from django.urls import path
from .views import UserProfileView, UserPasswordChangeView

urlpatterns = [
    path('', UserProfileView.as_view(), name='user-profile'),
    path('password/', UserPasswordChangeView.as_view(), name='user-password-change'),
]
