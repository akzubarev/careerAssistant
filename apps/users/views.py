from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.template.response import TemplateResponse

from apps.main.forms import NewUserForm


def profile(request):
    return TemplateResponse(request, 'users/profile.html', {})


def logout_view(request):
    logout(request)
    return redirect("main:main")


def auth(request, goal):
    if request.user.is_anonymous is False:
        return redirect("scoring:form", goal=goal)
    else:
        return TemplateResponse(request, 'users/auth.html', {"goal": goal})


def register_view(request, goal):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            if goal != "-":
                return redirect("scoring:form", goal=goal)
            else:
                return redirect("main:main")
        messages.error(request,
                       "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request,
                  template_name="users/register.html",
                  context={"register_form": form, "goal": goal})


def login_view(request, goal):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                if goal != "-":
                    return redirect("scoring:form", goal=goal)
                else:
                    return redirect("main:main")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()
    return render(request=request,
                  template_name="users/login.html",
                  context={"login_form": form, "goal": goal})
