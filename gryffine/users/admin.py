from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from users.models import ExtendedUser


class ExtendedUserInline(admin.StackedInline):
    model = ExtendedUser
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (ExtendedUserInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
