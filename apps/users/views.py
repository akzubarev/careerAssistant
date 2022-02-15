from django.template.response import TemplateResponse

from apps.recommendations.views import test_context


def main(request):
    return TemplateResponse(request, 'users/Profile.html', test_context)
