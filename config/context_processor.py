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
                    vacs = {vac.company.name: vac.name for vac in
                            list(recommendation_res.vacancies.all())[:6]}

                    articles = dict()
                    for article in recommendation_res.articles.all():
                        if article.description is not None and len(
                                articles.keys()) < 6:
                            articles[article.name] = article.description

                    model_res = {  # "Мероприятия":
                        "Вакансии": vacs,
                        "Обучение": articles
                    }
                    return {"goal": goal, "model_res": model_res}
    return {"goal": "None", "model_res": "None"}
