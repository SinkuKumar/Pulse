import datetime
from django.utils import timezone

class LastSeenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        user = getattr(request, "user", None)
        if user and user.is_authenticated:
            now = timezone.now()
            if not user.profile.last_seen or (now - user.profile.last_seen) > datetime.timedelta(minutes=5):
                user.profile.last_seen = now
                user.profile.save(update_fields=["last_seen"])

        return response
