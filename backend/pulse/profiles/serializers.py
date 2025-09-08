from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    skills_list = serializers.ListField(
        source="get_skills_list", read_only=True
    )

    class Meta:
        model = Profile
        fields = [
            "id", "user", "phone", "date_of_birth", "bio", "skills", "skills_list",
            "status", "last_seen"
        ]
        read_only_fields = ["last_seen"]
