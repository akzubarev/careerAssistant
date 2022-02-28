from django.db.models import Model
from apps.recommendations.models import Course
from tableparsing.parsers.BaseParser import Parser


class CourseParser(Parser):
    link = r'./data/not_user_data/courses.xlsx'
    modelClass: Model = Course
    fieldsets = {
        "name": "Название",
        "profile": "Отрасль",
        "description": "Описание для анонса",
        "tags": "Теги",
        "link": "Внешняя ссылка",
        "type": "Тип",
    }

    def handle_field(self, name: str, value):
        if name == "tags":
            value = [value]
        return value
