from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "user", "favorite_cuisine", "dietary_preferences"]
        read_only_fields = ["user"]
