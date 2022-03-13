import time

from django.shortcuts import redirect
from django.template.response import TemplateResponse

from apps.recommendations.views import recommendation
from apps.scoring.models import ScoringResult, FormResult
from apps.scoring.scoring_model import CareerScoring


def form(request):
    return TemplateResponse(request, 'scoring/Form.html', {})


def processing(request):
    if request.method == "POST":
        print(request.POST)
        data = {key: value for key, value in request.POST.items() if
                key != "csrfmiddlewaretoken"}
        print(data)
        # company = data.get('company')
        # sphere = data.get('sphere')
        # direction = data.get('direction')
        # level = data.get('level')
        print(" ".join(data.values()))
        form_res = FormResult.objects.create(
            user=request.user,
            jobs=[{
                'position': 'веб-дизайнер',
                'exp': 24,
                'achievements': 'работал в Adobe Photoshop'
            }],
            skills='Adobe Photoshop, Figma, теория ui/ux дизайна, python начальный уровень, HTML, CSS',
            additional=['Введение в веб-дизайн', 'Figma'],
            career_area=None
        )
        for competition in []:
            form_res.competitions.add(competition)

    return TemplateResponse(request, 'scoring/Processing.html', {})


def score(form_res: FormResult):
    scoring_model = CareerScoring('apps/scoring/data/')
    goals, result = scoring_model.get_career_goal(
        jobs=form_res.jobs,
        skills=form_res.skills,
        competitions=[c.name for c in form_res.competitions.all()],
        additional_education=form_res.additional,
        career_area=form_res.career_area
    )
    ScoringResult.objects.create(user=form_res.user,
                                 formResult=form_res,
                                 profiles=goals)


def scoring(request):
    formResult = FormResult.objects.filter(user=request.user).last()
    score(form_res=formResult)
    # scoring_res = formResult.score.first()
    # while scoring_res is None or scoring_res.recommendation.first() is None:
    #     time.sleep(1)
    return redirect("recommendations:recommendations")
