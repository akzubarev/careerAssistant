from django.db.models import Model

from apps.recommendations.models import Vacancy
from apps.users.models import Company
from tableparsing.parsers.BaseParser import Parser


class VacancyParser(Parser):
    link = r'./data/not_user_data/jobs.xlsx'
    modelClass: Model = Vacancy
    fieldsets = {"name": "Название",
                 "profile": "Отрасли компании",
                 # "description": "-",
                 # "Детальное описание"
                 "tags": "Теги",
                 "link": "Внешняя ссылка",
                 "company": "Компания",
                 "profession": "Профессия",
                 "branch": "Сфера деятельности",
                 "experience": "Опыт работы",
                 # "type": "-",
                 "shift": "Занятость",
                 "city": "Город"}

    def handle_field(self, name: str, value):
        if name == "company":
            value = self.handle_company(value=value)
        elif name == "experience":
            value = 1 if isinstance(value, str) and "1" in value else 0
        return value
