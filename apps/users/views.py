from django.template.response import TemplateResponse


def main(request):
    return TemplateResponse(request, 'users/Profile.html',
                            {"events_list": range(3),
                             "courses_list": range(3),
                             "vaccancies_list": range(3)})
