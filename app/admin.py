from django.contrib import admin

from app.models import ToDo, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "first_name", "last_name")
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("username", "email", "first_name", "last_name")
    ordering = ("id",)
    fieldsets = (
        (
            None,
            {"fields": ("username", "email", "first_name", "last_name", "password")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {"fields": ("username", "email", "first_name", "last_name", "password")},
        ),
    )


@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "user",
        "done",
        "created_at",
        "updated_at",
    )
    search_fields = ("title", "description", "user", "done")
    list_filter = ("title", "description", "user", "done")
    ordering = ("id",)
    fieldsets = ((None, {"fields": ("title", "description", "user", "done")}),)
    add_fieldsets = ((None, {"fields": ("title", "description", "user", "done")}),)
