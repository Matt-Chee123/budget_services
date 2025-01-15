from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = [
        field.name for field in CustomUser._meta.get_fields()
        if field.concrete and not field.many_to_many and field.name != 'password'
    ]