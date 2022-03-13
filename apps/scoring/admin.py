from django.contrib import admin

from apps.scoring.models import ScoringResult, FormResult


@admin.register(FormResult)
class FormResultAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        # 'company',
        'jobs_format',
        'skills',
        'competitions_format',
        'additional',
        'career_area'
    ]
    fieldsets = [
        ['Data', {
            'fields': [
                'user',
                # 'company',
                'jobs',
                'skills',
                'competitions',
                'additional',
                'career_area'
            ]}]
    ]

    @admin.display(description="Competitions", ordering="competitions")
    def competitions_format(self, obj):
        names = [competition.name for competition in obj.competitions.all()]
        res = ",".join(names)
        if len(res) == 0:
            res = "-"
        return res

    @admin.display(description="Jobs", ordering="jobs")
    def jobs_format(self, obj):
        names = [f'{job.get("position")}:{job.get("exp")}\n' for job in
                 obj.jobs]
        res = ",".join(names)
        if len(res) == 0:
            res = "-"
        return res


@admin.register(ScoringResult)
class ScoringResultAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'formResult_format',
        'profiles',
    ]
    fieldsets = [
        ['Data', {
            'fields': [
                'user',
                'formResult',
                'profiles',
            ]}]
    ]

    @admin.display(description="formResult", ordering="formResult")
    def formResult_format(self, obj):
        return obj.formResult.withLink()
