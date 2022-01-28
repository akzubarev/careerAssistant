from django.template.response import TemplateResponse


def main(request):
    return TemplateResponse(request,
                            'recomendations/RecomendationResult.html', {})


def stub(request):
    return TemplateResponse(request, 'recomendations/Stub.html', {})
