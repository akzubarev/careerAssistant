from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.main, name="main"),
    path('auth', views.auth, name="auth"),
    path("register", views.register_view, name="register"),
    path("login", views.login_view, name="login")
]
