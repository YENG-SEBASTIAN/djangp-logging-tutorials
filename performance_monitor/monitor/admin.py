from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group

admin.site.site_header = _('HMS')
admin.site.index_title = _('HMS Dashboard')

class CustomUserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'groups')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}
        ),
    )
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(User, CustomUserAdmin)