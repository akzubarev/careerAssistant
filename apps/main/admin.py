from django.contrib import admin

from .models import Event, Article, Course, Vacancy


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'profile',
        'tags',
        'type',
        'date',
        'company',
        'city',
        'link',
        'description',
    ]
    fieldsets = [
        ['Base', {
            'fields': [
                'name',
                'profile',
                'description',
                'tags',
                'link',
            ]}],
        ['Data', {
            'fields': [
                'type',
                'date',
                'company',
                'city',
            ]}]
    ]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'profile',
        'tags',
        # 'relatedArticles',
        'rubric',
        'link',
        'description',
    ]
    fieldsets = [
        ['Base', {
            'fields': [
                'name',
                'profile',
                'description',
                'tags',
                'link',
            ]}],
        ['Data', {
            'fields': [
                'type',
                'date',
                'company',
                'city',
            ]}]
    ]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'profile',
        'description',
        'tags',
        'link',
        'type'
    ]
    fieldsets = [
        ['Base', {
            'fields': [
                'name',
                'profile',
                'description',
                'tags',
                'link',
            ]}],
        ['Data', {
            'fields': [
                'type'
            ]}]
    ]


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'profile',
        'description',
        'tags',
        'link',
        'company_fmt',
        'profession',
        'branch',
        'experience',
        'type',
        'shift',
        'city',
    ]
    fieldsets = [
        ['Base', {
            'fields': [
                'name',
                'profile',
                'description',
                'tags',
                'link',
            ]}],
        ['Data', {
            'fields': [
                'company',
                'profession',
                'branch',
                'experience',
                'type',
                'shift',
                'city',
            ]}]
    ]

    @admin.display(description="Company")
    def company_fmt(self, obj):
        return obj.company.withLink()
