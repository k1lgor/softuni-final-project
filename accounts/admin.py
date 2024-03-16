from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFilters(admin.SimpleListFilter):
    # Define options
    title = "User Filters"

    # Parameter for the filter that will be used in the queryset
    parameter_name = "user_filter"

    def lookups(self, request, model_admin):
        return [
            ("email__icontains", "Email (contains)"),
            ("is_staff", "Is staff"),
        ]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(**{self.parameter_name: self.value()})

        return queryset


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "is_staff",
    )
    list_filter = (UserFilters,)
    ordering = ("name",)
    search_fields = [
        "name",
        "email",
    ]
