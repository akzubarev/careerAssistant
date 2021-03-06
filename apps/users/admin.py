from django.contrib import admin

from apps.users.models import User, Company


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'email',
        'first_name',
        'last_name',
        'is_staff',
    ]
    fieldsets = [
        ['Data', {
            'fields': [
                'username',
                'email',
                'first_name',
                'last_name',
                'is_staff',
            ]}]
    ]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'profile',
        'description',
        'tags',
    ]
    fieldsets = [
        ['Data', {
            'fields': [
                'name',
                'profile',
                'description',
                'tags',
            ]}]
    ]
