from django.template.response import TemplateResponse



def form(request):
    return TemplateResponse(request, 'scoring/Form.html', {})
