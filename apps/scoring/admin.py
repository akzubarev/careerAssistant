from django.contrib import admin

from apps.scoring.models import ScoringResult, FormResult


@admin.register(FormResult)
class FormResultAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        # 'company',
        'jobs_format',
        'skills',
        'competitions',
        'additional',
        'career_area',
        'updated_at',
        'created_at'
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
            ]}],
        ['Time', {
            'fields': [
                'updated_at',
                'created_at'
            ]
        }],
    ]

    @admin.display(description="Jobs", ordering="jobs")
    def jobs_format(self, obj):
        names = [f'{job.get("position")} - {job.get("exp")} мес.\n' for job in
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
        'updated_at',
        'created_at'
    ]
    fieldsets = [
        ['Data', {
            'fields': [
                'user',
                'formResult',
                'profiles',
            ]}],
        ['Time', {
            'fields': [
                'updated_at',
                'created_at'
            ]
        }],
    ]

    @admin.display(description="formResult", ordering="formResult")
    def formResult_format(self, obj):
        return obj.formResult.withLink()
