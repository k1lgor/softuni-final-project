from django.test import TestCase
from .models import Category
from django.core.exceptions import ObjectDoesNotExist

class CategoryModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Test Category")

    def test_category_name(self):
        self.assertEqual(str(self.category), self.category.name)

    def test_verbose_name(self):
        self.assertEqual(Category._meta.verbose_name, "Category")

    def test_verbose_name_plural(self):
        self.assertEqual(Category._meta.verbose_name_plural, "Categories")

    # def test_invalid_data(self):
    #     with self.assertRaises(ValueError):
    #         Category.objects.create(
    #             name=""
    #         )

    # def test_missing_fields(self):
    #     with self.assertRaises(ValueError):
    #         category = Category(name="Test Category")
    #         category.save()

    def test_non_existing_category(self):
        with self.assertRaises(ObjectDoesNotExist):
            Category.objects.get(
                id=999
            )
