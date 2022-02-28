from django.db.models import Model
from apps.recommendations.models import Article
from tables.handlers.Base import Parser, Exporter


class ArticleParser(Parser):
    link = r'./data/not_user_data/articles.xlsx'
    modelClass: Model = Article
    fieldsets = {
        "name": "Название",
        "profile": "Отрасль",
        "description": "Описание для анонса",
        "tags": "Теги",
        "link": "Внешняя ссылка",
        # "relatedArticles": "",
        "rubric": "Рубрики",
    }

    def handle_field(self, name: str, value):
        if name == "tags":
            value = [value]
        return value


class ArticleExporter(Exporter):
    filename = 'articles'
    modelClass: Model = Article
    fieldsets = {
        "name": "Название",
        "profile": "Отрасль",
        "description": "Описание для анонса",
        "tags": "Теги",
        "link": "Внешняя ссылка",
        # "relatedArticles": "",
        "rubric": "Рубрики",
    }
