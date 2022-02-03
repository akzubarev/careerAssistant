# Create your views here.
from django.template.response import TemplateResponse


def main(request):
    return TemplateResponse(request, 'main/MainPage.html', {})


def register(request):
    return TemplateResponse(request, 'scoring/Registration.html', {})
