from django.template.response import TemplateResponse


def main(request):
    return TemplateResponse(request,
                            'scoring/../main/templates/main/MainPage.html', {})


def form(request):
    return TemplateResponse(request, 'scoring/Form.html', {})


def register(request):
    return TemplateResponse(request, 'scoring/Registration.html', {})
