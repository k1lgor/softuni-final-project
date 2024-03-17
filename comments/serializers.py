from rest_framework import serializers

from profiles.serializers import ProfileSerializer

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "content", "recipe", "owner"]
        read_only_fields = ["owner"]
