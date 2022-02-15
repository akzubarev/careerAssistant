from django.template.response import TemplateResponse

test_context = {"events_list": range(3),
                "courses_list": range(3),
                "vaccancies_list": range(3),
                "model_res": {
                    "Мероприятия": {
                        "Как стать аналитиком данных и построить карьеру в IT": "Узнайте, как освоить профессию и начать работать в перспективной сфере, на вебинаре",
                        "KPMG Advisory School": "  Ты сможешь погрузиться в искусство бизнеса на KPMG Advisory School.",
                        "Бизнес-аналитик": "Станьте специалистом, который влияет на работу целых корпораций, всего за шесть месяцев",
                    },
                    "Обучение": {
                        "Как стать аналитиком данных и построить карьеру в IT": "Узнайте, как освоить профессию и начать работать в перспективной сфере, на вебинаре",
                        "KPMG Advisory School": "  Ты сможешь погрузиться в искусство бизнеса на KPMG Advisory School.",
                        "Бизнес-аналитик": "Станьте специалистом, который влияет на работу целых корпораций, всего за шесть месяцев",
                    },
                    "Вакансии": {
                        "Как стать аналитиком данных и построить карьеру в IT": "Узнайте, как освоить профессию и начать работать в перспективной сфере, на вебинаре",
                        "KPMG Advisory School": "  Ты сможешь погрузиться в искусство бизнеса на KPMG Advisory School.",
                        "Бизнес-аналитик": "Станьте специалистом, который влияет на работу целых корпораций, всего за шесть месяцев",
                    },
                }}


def main(request):
    return TemplateResponse(request,
                            'recommendations/RecommendationPage.html',
                            test_context)


def stub(request):
    return TemplateResponse(request, 'recommendations/Stub.html', {})
