def user_context(request):
    user = request.user
    username = user.username if not user.is_anonymous else "None"
    return {"username": username}


def recomendation_context(request):
    user = request.user
    if not user.is_anonymous:
        scoring_res = user.scoring_results.first()
        if scoring_res is not None:
            recommendation_res = scoring_res.recommendation.first()

    return {
        "goal": "Senior бизнес-аналитик в Тинькофф",
        "model_res": {
            "Мероприятия": {
                "Как стать аналитиком данных и построить карьеру в IT": "Узнайте, как освоить профессию и начать работать в перспективной сфере, на вебинаре",
                "KPMG Advisory School": "Ты сможешь погрузиться в искусство бизнеса на KPMG Advisory School.",
                "Бизнес-аналитик": "Станьте специалистом, который влияет на работу целых корпораций, всего за шесть месяцев",
            },
            "Обучение": {
                "Как стать аналитиком данных и построить карьеру в IT": "Узнайте, как освоить профессию и начать работать в перспективной сфере, на вебинаре",
                "KPMG Advisory School": "Ты сможешь погрузиться в искусство бизнеса на KPMG Advisory School.",
                "Бизнес-аналитик": "Станьте специалистом, который влияет на работу целых корпораций, всего за шесть месяцев",
            },
            "Вакансии": {
                "Как стать аналитиком данных и построить карьеру в IT": "Узнайте, как освоить профессию и начать работать в перспективной сфере, на вебинаре",
                "KPMG Advisory School": "Ты сможешь погрузиться в искусство бизнеса на KPMG Advisory School.",
                "Бизнес-аналитик": "Станьте специалистом, который влияет на работу целых корпораций, всего за шесть месяцев",
            },
        }}
