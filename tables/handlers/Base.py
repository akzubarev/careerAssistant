import abc
import math
from abc import ABC
from typing import Type

import pandas as pd
from django.db.models import Model
from pandas import DataFrame

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
            try:
                model.save()
            except Exception as e:
                print(e)

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


class Exporter:
    filename: str
    modelClass: Model
    fieldsets: dict

    def export(self, format):
        rows = list()
        for item in self.modelClass.objects.all():
            row = {
                data_key: self.handle_field(name=key, value=getattr(item, key))
                for key, data_key in
                self.fieldsets.items()
            }
            rows.append(row)

        df = pd.DataFrame(rows)
        if format == "pandas":
            return df
        elif format == "xlsx":
            name = f"output/{self.filename}.xlsx"
            df.to_excel(name)
            return name
        else:
            raise ValueError()

    @abc.abstractmethod
    def handle_field(self, name: str, value):
        return value
