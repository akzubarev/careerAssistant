from django.contrib import admin

from apps.recommendations.models import RecommendationResult


@admin.register(RecommendationResult)
class RecommendationResultAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'scoringResult_format',
        # 'events_format',
        'articles_format',
        # 'courses_format',
        'vacancies_format',
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

    @admin.display(description="scoringResult", ordering="scoringResult")
    def scoringResult_format(self, obj):
        return obj.scoringResult.withLink()

    @admin.display(description="Events", ordering="events")
    def events_format(self, obj):
        return ",".join(event.name for event in obj.events.all())

    @admin.display(description="Articles", ordering="articles")
    def articles_format(self, obj):
        return ",".join(article.name for article in list(obj.articles.all())[:6])

    @admin.display(description="Courses", ordering="courses")
    def courses_format(self, obj):
        return ",".join(course.name for course in obj.courses.all())

    @admin.display(description="Vacancies", ordering="vacancies")
    def vacancies_format(self, obj):
        return ",".join(vacancy.name for vacancy in obj.vacancies.all())
