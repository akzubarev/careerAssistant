from apps.main.models import Vacancy
from apps.recommendations.models import RecommendationResult
from apps.scoring.models import FormResult, ScoringResult


def user_context(request):
    user = request.user
    username = user.username if not user.is_anonymous else "None"
    return {"username": username}


def recomendation_context(request):
    user = request.user
    if not user.is_anonymous:
        form_res: FormResult = user.form_results.order_by(
            "-created_at").first()
        if form_res is not None:
            scoring_res: ScoringResult = form_res.score.order_by(
                "-created_at").first()
            if scoring_res is not None:
                recommendation_res: RecommendationResult = scoring_res. \
                    recommendation.order_by("-created_at").first()
                if recommendation_res is not None:
                    top_pick: Vacancy = recommendation_res.vacancies.first()
                    if top_pick is not None:
                        goal = f"{top_pick.name} в {top_pick.company.name}"
                    else:
                        goal = "Цель не была определена"
                    # vacs = {
                    #     "Как стать аналитиком данных и построить карьеру в IT": "Узнайте, как освоить профессию и начать работать в перспективной сфере, на вебинаре",
                    #     "KPMG Advisory School": "Ты сможешь погрузиться в искусство бизнеса на KPMG Advisory School.",
                    #     "Бизнес-аналитик": "Станьте специалистом, который влияет на работу целых корпораций, всего за шесть месяцев",
                    # }
                    vacs = {vac.company.name: vac.name for vac in
                            recommendation_res.vacancies.all()}

                    articles = {
                        article.name: (
                            article.description if article.description is not None else "")
                        for article in recommendation_res.articles.all()}

                    model_res = {
                        # "Мероприятия": {
                        #     "Как стать аналитиком данных и построить карьеру в IT":
                        #     "Узнайте, как освоить профессию и начать работать в перспективной сфере, на вебинаре",
                        #     "KPMG Advisory School":
                        #     "Ты сможешь погрузиться в искусство бизнеса на KPMG Advisory School.",
                        #     "Бизнес-аналитик":
                        #     "Станьте специалистом, который влияет на работу целых корпораций, всего за шесть месяцев",
                        # },
                        "Вакансии": vacs,
                        "Обучение": articles
                    }
                    return {"goal": goal, "model_res": model_res}
    return {"goal": "None", "model_res": "None"}
