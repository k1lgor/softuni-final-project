from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_cuisine = models.CharField(max_length=100)
    dietary_preferences = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.name}'s Profile"
