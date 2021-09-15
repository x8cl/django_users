from django.contrib import admin
from .models import User

# Register your models here.
""" class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ("email", "username", "name", "lname",)
    list_filter = ("email", "username", "name", "lname", "is_active",)
    ordering = ("-created_at",)
    list_display = ("email", "username", "name", "lname", "is_active",)
    fieldsets = ((None, {"fields": ("email", "username", "name", "name2", "lname", "lname2",)}),
        ("Permissions", {"fields": ("user_lvl", "is_active")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "name", "name2", "lname", "lname2", "password", "user_lvl", "is_active")}
         ),
    )

 """
admin.site.register(User)