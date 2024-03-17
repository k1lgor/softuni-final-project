from django.test import TestCase

from accounts.admin import User
from categories.models import Category
from recipes.models import Recipe

from .models import Comment


class CommentModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="testuser@localhost",
            name="testuser",
            password="testpassword",
        )
        self.category = Category.objects.create(name="Test Category")
        self.recipe = Recipe.objects.create(
            title="Test Recipe",
            description="Test description",
            ingredients="Test ingredients",
            instructions="Test instructions",
            cooking_time=10,
            category=self.category,
            user=self.user,
        )

    def test_comment_creation(self):
        comment = Comment.objects.create(
            recipe=self.recipe,
            user=self.user,
            content="Test comment content",
        )
        self.assertTrue(isinstance(comment, Comment))
        self.assertEqual(comment.recipe, self.recipe)
        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.content, "Test comment content")

    def test_comment_str_method(self):
        comment = Comment.objects.create(
            recipe=self.recipe,
            user=self.user,
            content="Test comment content",
        )
        self.assertEqual(
            str(comment), f"Comment by {self.user.name} on recipe '{self.recipe.title}'"
        )
