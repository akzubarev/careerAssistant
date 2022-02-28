from django.template.response import TemplateResponse


def main(request):
    return TemplateResponse(request,
                            'recommendations/RecommendationPage.html', {})


def processing(request):
    if request.method == "POST":
        print(request.POST)
        data = {key: value for key, value in request.POST.items() if
                key != "csrfmiddlewaretoken"}
        # company = data.get('company')
        # sphere = data.get('sphere')
        # direction = data.get('direction')
        # level = data.get('level')
        print(" ".join(data.values()))
    return TemplateResponse(request, 'recommendations/Processing.html', {})
