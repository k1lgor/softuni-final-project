from django.contrib import admin

from .models import Category


class CategoryFilters(admin.SimpleListFilter):
    # Define options
    title = "Category Filters"

    # Parameter for the filter that will be used in the queryset
    parameter_name = "category_filter"

    def lookups(self, request, model_admin):
        return [("name__icontains", "Name (contains)")]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(**{self.parameter_name: self.value()})

        return queryset


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = (CategoryFilters,)
    ordering = ("name",)
    search_fields = ["name"]
