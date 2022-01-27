from django.contrib import admin

from apps.scoring.models import ScoringResult


@admin.register(ScoringResult)
class ScoringResultAdmin(admin.ModelAdmin):
    list_display = [
        'company',
        'profile',
        'position',
        'experience',
        'education',
        'scores',
        'preferences'
    ]
    fieldsets = [
        ['Data', {
            'fields': [
                'company',
                'profile',
                'position',
                'experience',
                'education',
                'scores',
                'preferences'
            ]}]
    ]
