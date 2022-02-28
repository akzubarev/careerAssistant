from django.db.models import Model
from apps.users.models import Company
from tables.handlers.Base import Parser, Exporter


class CompanyParser(Parser):
    link = r'./data/not_user_data/companies.xlsx'
    modelClass: Model = Company
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


class CompanyExporter(Exporter):
    filename = 'companies'
    modelClass: Model = Company
    fieldsets = {
        "name": "Название",
        "profile": "Отрасль",
        "description": "Описание для анонса",
        "tags": "Теги",
    }
