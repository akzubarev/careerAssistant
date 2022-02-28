import os
import sys

import django

sys.path[0] += '/../../..'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

import tableparsing.parsers as parsers


def main():
    # parsers.VacancyParser().parse()
    # parsers.CompanyParser().parse()
    # parsers.CourseParser().parse()
    # parsers.EventParser().parse()
    parsers.ArticleParser().parse()


if __name__ == "__main__":
    main()
