from django.template.response import TemplateResponse


def main(request):
    return TemplateResponse(request,
                            'recommendations/templates/recommendations/RecommendationResult.html', {})


def stub(request):
    return TemplateResponse(request,
                            'recommendations/templates/recommendations/Stub.html', {})
