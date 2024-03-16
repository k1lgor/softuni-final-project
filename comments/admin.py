from django.contrib import admin

from .models import Comment


class CommentFilters(admin.SimpleListFilter):
    # Define options
    title = "Comment Filters"

    # Parameter for the filter that will be used in the queryset
    parameter_name = "comment_filter"

    def lookups(self, request, model_admin):
        return [
            ("recipe", "Recipe"),
            ("user", "User"),
        ]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(**{self.parameter_name: self.value()})

        return queryset


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "recipe",
        "user",
    )
    list_filter = (CommentFilters,)
    ordering = ("recipe",)
    search_fields = ["comment"]
