from django.db import models

from accounts.models import User
from categories.models import Category


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=False, null=False)
    ingredients = models.TextField(blank=False, null=False)
    instructions = models.TextField(blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
