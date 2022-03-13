from django.urls import path
from apps.users import views

app_name = "users"
urlpatterns = [
    path('', views.profile),
    path('<goal>/auth', views.auth, name="auth"),
    path("<goal>/register", views.register_view, name="register"),
    path("<goal>/login", views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
]
