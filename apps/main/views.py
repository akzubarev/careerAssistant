# Create your views here.
from django.template.response import TemplateResponse


def main(request):
    return TemplateResponse(request, 'main/MainPage.html',
                            {"how_to_help_list": range(3)})


def register(request):
    return TemplateResponse(request, 'main/Registration.html', {})
