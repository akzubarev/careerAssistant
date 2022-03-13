from django.template.response import TemplateResponse


def recommendation(request):
    return TemplateResponse(request,
                            'recommendations/RecommendationPage.html', {})
