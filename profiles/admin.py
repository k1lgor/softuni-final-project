from django.contrib import admin

from .models import Profile


class ProfileFilters(admin.SimpleListFilter):
    # Define options
    title = "Profile Filters"

    # Parameter for the filter that will be used in the queryset
    parameter_name = "profile_filter"

    def lookups(self, request, model_admin):
        return [
            ("favorite_cuisine__exact", "Favorite cuisine"),
            ("dietary_preferences__exact", "Dietary preferences"),
        ]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(**{self.parameter_name: self.value()})

        return queryset


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "favorite_cuisine",
        "dietary_preferences",
    )
    list_filter = (ProfileFilters,)
    ordering = ("user",)
    search_fields = ["favorite_cuisine", "dietary_preferences"]
