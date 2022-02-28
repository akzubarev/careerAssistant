import os
import sys

import django

sys.path[0] += '/../../..'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

import tables.handlers as handlers


def main():
    # handlers.VacancyParser().parse()
    # handlers.CompanyParser().parse()
    # handlers.CourseParser().parse()
    # handlers.EventParser().parse()
    # handlers.ArticleParser().parse()

    df = handlers.VacancyExporter().export(format="pandas")
    print(df.head())
    df = handlers.CompanyExporter().export(format="pandas")
    print(df.head())
    df = handlers.CourseExporter().export(format="pandas")
    print(df.head())
    df = handlers.EventExporter().export(format="pandas")
    print(df.head())
    df = handlers.ArticleExporter().export(format="pandas")
    print(df.head())

    handlers.VacancyExporter().export(format="xlsx")
    handlers.CompanyExporter().export(format="xlsx")
    handlers.CourseExporter().export(format="xlsx")
    handlers.EventExporter().export(format="xlsx")
    handlers.ArticleExporter().export(format="xlsx")


if __name__ == "__main__":
    main()
