from django.shortcuts import redirect
from django.template.response import TemplateResponse

from apps.scoring.models import ScoringResult, FormResult
from apps.scoring.scoring_model import CareerScoring


def form(request, goal):
    if goal == "goal":
        return TemplateResponse(request, 'scoring/formGoal.html', {})
    else:
        return TemplateResponse(request, 'scoring/formNoGoal.html', {})


def processing(request):
    if request.method == "POST":
        data = {key: value for key, value in request.POST.items() if
                key != "csrfmiddlewaretoken"}
        # print(data)
        jobs = list()
        for i in range(3):
            if f"profile_{i}" in data.keys():
                job = {
                    'position': data.get(f"profile_{i}"),
                    'exp': data.get(f"experience_{i}"),
                    'achievements': data.get(f"duties_{i}")
                }
                jobs.append(job)

        FormResult.objects.create(
            user=request.user, jobs=jobs, skills=data.get("skills"),
            additional=[], career_area=data.get("field"),
            competitions=data.get("competitions")
        )

    return TemplateResponse(request, 'scoring/processing.html', {})


def score(form_res: FormResult):
    scoring_model = CareerScoring('apps/scoring/data/')
    competitions = form_res.competitions
    if competitions is not None and len(competitions) > 0:
        print(competitions)
        competitions = [{'name': comp.split(" - ")[0],
                         'achievement': comp.split(" - ")[1]
                         } for comp in competitions]
    else:
        competitions = list()

    goals, result = scoring_model.get_career_goal(
        jobs=form_res.jobs,
        skills=form_res.skills,
        competitions=competitions,
        additional_education=form_res.additional,
        career_area=form_res.career_area
    )
    ScoringResult.objects.create(user=form_res.user,
                                 formResult=form_res,
                                 profiles=goals)


def scoring(request):
    formResult = FormResult.objects.filter(user=request.user).order_by(
        "-created_at").first()
    score(form_res=formResult)

    return redirect("recommendations:recommendations")
