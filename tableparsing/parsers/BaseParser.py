import abc
import math
from abc import ABC
from typing import Type

import pandas as pd
from django.db.models import Model

from apps.users.models import Company


class Parser(ABC):
    link: str
    modelClass: Type[Model]
    fieldsets: dict

    def parse(self):
        df = pd.read_excel(self.link)  # , engine='openpyxl')
        for index, row in df.iterrows():
            model = self.modelClass()
            for key, data_key in self.fieldsets.items():
                val = row.get(data_key)
                if isinstance(val, float) and math.isnan(val):
                    val = None
                val = self.handle_field(name=key, value=val)
                setattr(model, key, val)
            # try:
            #
            # except Exception as e:
            #     print(e)
            model.save()

    @abc.abstractmethod
    def handle_field(self, name: str, value):
        return value

    def handle_company(self, value):
        company = None
        if value is not None:
            idx = value.find("[") - 1
            name = value[0:idx]
            company = Company.objects.filter(name=name).first()
        return company
