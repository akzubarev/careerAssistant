from django.template.response import TemplateResponse


def main(request):
    return TemplateResponse(request, 'users/Profile.html', {})
