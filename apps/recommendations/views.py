from django.template.response import TemplateResponse

from apps.main.models import Vacancy, Article
from apps.recommendations.models import RecommendationResult
from apps.scoring.models import FormResult, ScoringResult
from apps.recommendations.recommendation_system import RecommendationSystem
from apps.users.models import Company


def find_or_create_vacancy(company_name, vac_name):
    company = Company.objects.filter(name=company_name).first()
    if company is None:
        company = Company.objects.create(name=company_name)

    vacancy = Vacancy.objects.filter(name=vac_name,
                                     company__name=company_name).first()
    if vacancy is None:
        vacancy = Vacancy.objects.create(name=vac_name, company=company)
    return vacancy


def recommend(scoring_res: ScoringResult, form_res: FormResult):
    jobs = list()
    for job in form_res.jobs:
        jobs.append(f"{job.get('company')} {job.get('position')}")
    exp = "; ".join(jobs)

    recommender = RecommendationSystem('data/')
    vacancies = recommender.recommend_vacancies(
        scoring_result=scoring_res.profiles
    )
    articles = recommender.recommend_articles(skills=exp)
    result = RecommendationResult.objects.create(scoringResult=scoring_res)

    for vac in vacancies:
        vacancy = find_or_create_vacancy(company_name=vac.get("Компания"),
                                         vac_name=vac.get("Название"))
        result.vacancies.add(vacancy)

    for art_name in articles:
        article = Article.objects.filter(name=art_name).first()
        if article is None:
            article = Article.objects.create(name=art_name)
        result.articles.add(article)

    # result.events.add()
    # result.courses.add()
    result.save()
    return result


def recommendation(request):
    formResult = FormResult.objects.filter(user=request.user).order_by(
        "-created_at").first()
    if formResult is not None:
        scoringResult:ScoringResult = formResult.score.first()
        if scoringResult is not None:
            rec = scoringResult.recommendation.first()
            if rec is None:
                recommend(scoring_res=scoringResult, form_res=formResult)
    return TemplateResponse(request,
                            'recommendations/RecommendationPage.html', {})
