from datetime import datetime
import pytz
from django.db.models import Model
from apps.recommendations.models import Event
from tableparsing.parsers.BaseParser import Parser
from django.utils.timezone import make_aware


class EventParser(Parser):
    link = r'./data/not_user_data/events.xlsx'
    modelClass: Model = Event
    fieldsets = {
        "name": "Название",
        "profile": "Тип мероприятия",
        "description": "Описание для анонса",
        "tags": "Теги",
        "link": "Внешняя ссылка",
        "type": "Тип мероприятия",
        "date": "Дата начала события",
        "company": "Компания",
        "city": "Город",
    }

    def handle_field(self, name: str, value):
        if name == "company":
            value = self.handle_company(value=value)
        if name == "date":
            time = list(map(int, value.split(".")))
            naive = datetime(day=time[0], month=time[1], year=time[2])
            aware = make_aware(naive, timezone=pytz.timezone("Europe/Moscow"))
            value = aware
        return value
