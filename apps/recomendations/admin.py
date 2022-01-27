from django.contrib import admin

from apps.recomendations.models import Event, Article, Course, \
    Vacancy


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'profile',
        'description',
        'tags',
        'link',
        'type',
        'date',
        'company',
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
        'description',
        'tags',
        'link',
        # 'relatedArticles',
        'rubric'
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
        'company',
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
