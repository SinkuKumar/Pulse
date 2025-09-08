from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "status", "last_seen")
    search_fields = ("user__username", "phone", "skills")
    list_filter = ("status",)
