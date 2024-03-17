from django.test import TestCase
from categories.models import Category
from accounts.models import User
from .models import Recipe


class RecipeModelTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Test Category")
        self.user = User.objects.create(
            name="testuser",
            email="testuser@localhost",
            password="testpassword",
        )

    def test_recipe_str(self):
        recipe = Recipe.objects.create(
            title="Test Recipe 1",
            description="Test Description",
            ingredients="Test Ingredients",
            instructions="Test Instructions",
            category=self.category,
            user=self.user,
        )
        self.assertEqual(str(recipe), "Test Recipe 1")

    def test_recipe_fields(self):
        recipe = Recipe.objects.create(
            title="Test Recipe 2",
            description="Test Description",
            ingredients="Test Ingredients",
            instructions="Test Instructions",
            category=self.category,
            user=self.user,
        )
        self.assertEqual(recipe.title, "Test Recipe 2")
        self.assertEqual(recipe.description, "Test Description")
        self.assertEqual(recipe.ingredients, "Test Ingredients")
        self.assertEqual(recipe.instructions, "Test Instructions")
        self.assertEqual(recipe.cooking_time, 0)  # default value
        self.assertEqual(recipe.category, self.category)
        self.assertEqual(recipe.user, self.user)
