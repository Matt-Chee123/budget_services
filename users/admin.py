from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(UserAdmin):
    list_display = [
        field.name for field in UserProfile._meta.get_fields()
        if field.concrete and not field.many_to_many and field.name != 'password'
    ]