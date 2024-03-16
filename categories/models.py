from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Category"  # Change 'Categorys' to 'Category'
        verbose_name_plural = "Categories"  # Change 'Categorys' to 'Categories'

    def __str__(self):
        return self.name
