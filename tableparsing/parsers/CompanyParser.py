from django.db.models import Model
from apps.recommendations.models import Vacancy
from tableparsing.parsers.BaseParser import Parser


class CompanyParser(Parser):
    link = r'./data/not_user_data/companies.xlsx'
    modelClass: Model = Vacancy
    fieldsets = {
        "name": "Название",
        "profile": "Отрасль",
        "description": "Описание для анонса",
        "tags": "Отрасль",
    }

    def handle_field(self, name: str, value):
        if name == "tags":
            value = [value]
        return value
