from django.contrib import admin

from .models import Recipe


class RecipeFilters(admin.SimpleListFilter):
    # Define options
    title = "Recipe Filters"

    # Parameter for the filter that will be used in the queryset
    parameter_name = "recipe_filter"

    def lookups(self, request, model_admin):
        return [
            ("title__icontains", "Title (contains)"),
            ("category", "Category"),
            ("user", "User"),
        ]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(**{self.parameter_name: self.value()})

        return queryset


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "user",
    )
    list_filter = (RecipeFilters,)
    ordering = ("title",)
    search_fields = [
        "title",
        "description",
    ]
