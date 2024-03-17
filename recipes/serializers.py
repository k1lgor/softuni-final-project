from rest_framework import serializers

from profiles.serializers import ProfileSerializer

from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(read_only=True)

    class Meta:
        model = Recipe
        fields = [
            "id",
            "user",
            "description",
            "ingredients",
            "category",
            "instructions",
            "cooking_time",
            "owner",
        ]
        read_only_fields = ["owner"]
