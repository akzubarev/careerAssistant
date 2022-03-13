from django.contrib import admin

from apps.recommendations.models import RecommendationResult


@admin.register(RecommendationResult)
class RecommendationResultAdmin(admin.ModelAdmin):
    list_display = [
        'scoringResult',
        'events_format',
        # 'articles',
        # 'courses',
        # 'vacancies',
        'updated_at',
        'created_at'
    ]

    fieldsets = [
        ['Base', {
            'fields': [
                'scoringResult',
                'events',
                'articles',
                'courses',
                'vacancies',
            ]
        }],
        ['Time', {
            'fields': [
                'updated_at',
                'created_at'
            ]
        }],
    ]

    @admin.display(description="Events")
    def events_format(self, obj):
        return ",".join(event.name for event in obj.events.all())
