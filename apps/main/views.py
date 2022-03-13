from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.template.response import TemplateResponse

from apps.main.forms import NewUserForm


def main(request):
    return TemplateResponse(
        request, 'main/MainPage.html',
        {
            "how_to_help_list": {
                "Оцениваем тебя как профессионала": "Анализируем твои навыки, предпочтения, опыт работы",
                "Определяем карьерную цель для тебя": "Выбираем компанию, должность, сферу и направление работы",
                "Рассказываем как построить карьеру мечты": "Даем рекомендации по мероприятиям, курсам и вакансиям",
            }
        }
    )


def auth(request):
    return TemplateResponse(request, 'main/auth.html', {})


def register_view(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("scoring:form")
        messages.error(request,
                       "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="main/register.html",
                  context={"register_form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("scoring:form")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    elif request.user.is_anonymous is False:
        return redirect("scoring:form")

    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html",
                  context={"login_form": form})
