from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("busy", "Busy"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.TextField(help_text="Comma-separated skills", blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
    last_seen = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def get_skills_list(self):
        return [skill.strip() for skill in self.skills.split(",")] if self.skills else []
